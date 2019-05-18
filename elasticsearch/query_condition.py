#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月10日
@author: yangxu
'''
import datetime

def generate_condition_data(host,time_value):
    condition_data = {
        "sort": [
            {"save_timestamp":{"order":"asc"}}
                 ],
        "query": {
            "bool": {
                     "must": [
                            { "term":  { "host": host }}, 
                            {"range" : {"save_timestamp" : {
                                        "gte": (datetime.datetime.now()-datetime.timedelta(minutes=time_value)).strftime("%Y-%m-%d %H:%M:%S"), 
                                        "lte": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), }}},
                              ]
                     }
            
            }
    }
    return condition_data      