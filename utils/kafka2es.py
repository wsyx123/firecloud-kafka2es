#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on May 12, 2019

@author: yangxu
'''
import logging

'''
data save in elasticsearch format:

es 使用7以下版本还有type概念 ， 7及以上去除了type
两个不同type下的同名field，如：hostname, collect_time,save_time，在ES同一个索引下其实被认为是同一个filed,
你必须在两个不同的type中定义相同的filed映射。否则，不同type中的相同字段名称就会在处理中出现冲突的情况，导致Lucene处理效率下降。
去掉type就是为了提高ES处理数据的效率。

由于python elasticsearch api 只有7以下的，所以elasticsearch 用6.x ，index设计如下
---- index                type   
    cpu-load-yyyy-mm-dd   load
index 按照日期递增, 每个采集的index最多保留30天，即 30 个index ，过期的定时转存到hbase

每个采集都有hostname, collect_time 和  save_time
collect_time: time  是agent采集的时间
save_time:  time  数据发送到kafka后，server端从kafka获取然后保存到es的时间

 - cpu load
    load1: float   平均活动进程数, 单位 个
    load5: float
    load15: float
    
 - cpu usage
    idle: float   百分比
    user: float
    system: float
    iowait: float
    
 - memory usage
    virt_available: float   百分比
    virt_used: float
    swap_available: float
    swap_used: float
    
 - disk io
    tps: float    具体数值
    blks: float
    
 - disk usage
    available: float   百分比
    used: float
    
 - net io
    kb_sent: float  具体数值,单位  kb
    kb_recv: float
    
 - net conn
    LISTEN: integer
    ESTABLISHED: integer

 - process thread
    processes: integer
    threads: integer
    
'''

from kafka import KafkaConsumer
from elasticsearch.es_api import IndexApi
from elasticsearch.index_mapping import get_mapping
from datetime import datetime
import json

# def data_to_es(es_hosts,data_queue):
#     #es_hosts =  ["host1","host2"]
#     first_flag = True
#     es = Elasticsearch(es_hosts)
#     mapping = {
#         'properties': {
#             'save_timestamp': {
#                 'type': 'date'
#                 }
#             }
#         }
#     while True:
#         data = data_queue.get()
#         topic = data.topic
#         index = "{}-{}".format(topic, datetime.now().strftime("%Y-%m-%d"))
#         value = json.loads(data.value)
#         value["save_timestamp"] = datetime.now()
#         if first_flag:
#             es.indices.create(index=index, ignore=400)
#             es.indices.put_mapping(index=index, doc_type=topic, body=mapping)
#             first_flag = False
#         es.index(index=index, doc_type=topic, body=value)

def data_to_es(es_hosts,data_queue):
    host = es_hosts[0].split(":")[0]
    port = es_hosts[0].split(":")[1]
    while True:
        data = data_queue.get()
        topic = data.topic
        #按照月创建index
        index = "{}-{}".format(topic, datetime.now().strftime("%Y-%m"))
        value = json.loads(data.value)
        value["save_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #判断此index 是否存在，不存在则创建并设置mapping
        indexObj = IndexApi(host,port)
        #获取index，如果不存在返回的response status是  404
        ind_res = indexObj.iget(index)
        if ind_res["code"] == 404:
            mapping = get_mapping(topic)
            indexObj.icreate(index_name=index, mapping=mapping)
        #创建document
        doc_res = indexObj.dcreate(index_name=index, doc_type=topic, doc_id=None, doc_body=value)
        if doc_res["code"] == 400:
            logging.error(doc_res["result"])

        


def data_from_kafka(*topics,**kwargs):
    consumer = KafkaConsumer(*topics,bootstrap_servers=kwargs["kafka_hosts"])
    data_queue = kwargs["data_queue"]
    for msg in consumer:
        data_queue.put(msg)