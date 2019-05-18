#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import threading
import Queue
import os
from wsgiref.simple_server import make_server
from optparse import OptionParser
import json
import logging
from utils.logger import logger_config
from utils.kafka2es import data_from_kafka,data_to_es

#agent 简单状态查询api
def handle_request(environment,start_response):
    start_response('200 OK',[('Content-Type','text/plain')])
    try:
        request_body_size = int(environment.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    else:
        data_json = eval(environment['wsgi.input'].read(request_body_size))
        print data_json
    return json.dumps({"code":200})

#运行一个简单http server        
def run_server(port,handle_request):
    try:
        httpd = make_server('',port,handle_request)
        logging.info("Listen on : 0.0.0.0:{}".format(port))
        httpd.serve_forever()
    except Exception as e:
        logging.error(e.message)
        os._exit(1)
        
#启动kafka2es
def run_kafka2es(*topics,**kwargs):
    es = kwargs["es_hosts"]
    kafka_hosts = kwargs["kafka_hosts"]
    data_queue = Queue.Queue()
    t1 = threading.Thread(target=data_from_kafka, args=(topics),kwargs={"kafka_hosts":kafka_hosts,"data_queue":data_queue})
    t2 = threading.Thread(target=data_to_es, args=(es,data_queue))
    
    t1.start()
    t2.start()

def main():
    #第一次fork
    try:
        pid = os.fork()
        if pid > 0:
            os._exit(0)
    except OSError,error:
        logging.error( 'fork #1 failed: %d (%s)' % (error.errno, error.strerror))
        os._exit(1)
    os.chdir('/')
    os.setsid()
    os.umask(0)
    #第二次fork
    try:
        pid = os.fork()
        if pid > 0:
            os._exit(0)
    except OSError,error:
        logging.error( 'fork #2 failed: %d (%s)' % (error.errno, error.strerror))
        os._exit(1)
    
    #解析命令行输入参数
    parser = OptionParser()
    parser.add_option("-p","--port",dest="port",help="the agent listen port,default:7001",default=7001)
    parser.add_option("-e","--elasticsearch",dest="es",help="the register center of master server address,default:localhost:9200",
                      default="localhost:9200")
    parser.add_option("-k","--kafka",dest="kafka",help="the message queue server address of kafka,default:localhost:9092",
                      default="localhost:9092")
    parser.add_option("-l","--log",dest="log",help="the log file path,default:/var/log/kafka2es.log",default="/var/log/kafka2es.log")
    (options, args) = parser.parse_args()
    
    port = options.port
    es = options.es.split(",")
    kafka_hosts = options.kafka.split(",")
    logfile = options.log
    
    #日志初始化
    logger_config(logfile)
    
    #启动http server
    http_thread = threading.Thread(target=run_server,args=(port,handle_request))
    http_thread.start()
    
    #启动kafka消费、保存数据到es的  线程
    topics = ("cpu-load","cpu-usage","mem-usage",
              "disk-io","disk-usage","net-io",
              "net-conn","process-thread")
    kwargs = {"es_hosts":es,"kafka_hosts":kafka_hosts}
    run_kafka2es(*topics,**kwargs)
    


if __name__ == "__main__":
    main()

    
