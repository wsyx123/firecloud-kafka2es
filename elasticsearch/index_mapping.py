#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年4月10日
@author: yangxu
'''
cpu_load_mapping = {
        "settings" : {
            "index" : {
                "number_of_replicas" : 1 
                    }
                  },
        "mappings" : {
              "cpu-load" : {
                "properties" : {
                  "hostname" : {
                    "type" : "text"
                  },
                  "load1" : {
                    "type" : "float"
                  },
                  "load5" : {
                    "type" : "float"
                  },
                  "load15" : {
                    "type" : "float"
                  },
                  "collect_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  },
                  "save_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  }
                }
              }
            }
        }

cpu_usage_mapping = {
        "settings" : {
            "index" : {
                "number_of_replicas" : 1 
                    }
                  },
        "mappings" : {
              "cpu-usage" : {
                "properties" : {
                  "hostname" : {
                    "type" : "text"
                  },
                  "idle" : {
                    "type" : "float"
                  },
                  "user" : {
                    "type" : "float"
                  },
                  "system" : {
                    "type" : "float"
                  },
                  "iowait" : {
                    "type" : "float"
                  },
                  "collect_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  },
                  "save_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  }
                }
              }
            }
        }

mem_usage_mapping = {
        "settings" : {
            "index" : {
                "number_of_replicas" : 1 
                    }
                  },
        "mappings" : {
              "mem-usage" : {
                "properties" : {
                  "hostname" : {
                    "type" : "text"
                  },
                  "virt_available" : {
                    "type" : "float"
                  },
                  "virt_used" : {
                    "type" : "float"
                  },
                  "swap_available" : {
                    "type" : "float"
                  },
                  "swap_used" : {
                    "type" : "float"
                  },
                  "collect_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  },
                  "save_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  }
                }
              }
            }
        }

disk_io_mapping = {
        "settings" : {
            "index" : {
                "number_of_replicas" : 1 
                    }
                  },
        "mappings" : {
              "disk-io" : {
                "properties" : {
                  "hostname" : {
                    "type" : "text"
                  },
                  "tps" : {
                    "type" : "float"
                  },
                  "blks" : {
                    "type" : "float"
                  },
                  "collect_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  },
                  "save_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  }
                }
              }
            }
        }


disk_usage_mapping = {
        "settings" : {
            "index" : {
                "number_of_replicas" : 1 
                    }
                  },
        "mappings" : {
              "disk-usage" : {
                "properties" : {
                  "hostname" : {
                    "type" : "text"
                  },
                  "available" : {
                    "type" : "float"
                  },
                  "used" : {
                    "type" : "float"
                  },
                  "collect_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  },
                  "save_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  }
                }
              }
            }
        }

net_io_mapping = {
        "settings" : {
            "index" : {
                "number_of_replicas" : 1 
                    }
                  },
        "mappings" : {
              "net-io" : {
                "properties" : {
                  "hostname" : {
                    "type" : "text"
                  },
                  "kb_sent" : {
                    "type" : "float"
                  },
                  "kb_recv" : {
                    "type" : "float"
                  },
                  "collect_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  },
                  "save_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  }
                }
              }
            }
        }

net_conn_mapping = {
        "settings" : {
            "index" : {
                "number_of_replicas" : 1 
                    }
                  },
        "mappings" : {
              "net-conn" : {
                "properties" : {
                  "hostname" : {
                    "type" : "text"
                  },
                  "ESTABLISHED" : {
                    "type" : "integer"
                  },
                  "LISTEN" : {
                    "type" : "integer"
                  },
                  "collect_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  },
                  "save_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  }
                }
              }
            }
        }

process_thread_mapping = {
        "settings" : {
            "index" : {
                "number_of_replicas" : 1 
                    }
                  },
        "mappings" : {
              "process-thread" : {
                "properties" : {
                  "hostname" : {
                    "type" : "text"
                  },
                  "processes" : {
                    "type" : "integer"
                  },
                  "threads" : {
                    "type" : "integer"
                  },
                  "collect_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  },
                  "save_time" : {
                    "type" : "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                  }
                }
              }
            }
        }

def get_mapping(topic):
    type_dict = {
        "cpu-load":cpu_load_mapping,
        "cpu-usage":cpu_usage_mapping,
        "mem-usage":mem_usage_mapping,
        "disk-io":disk_io_mapping,
        "disk-usage":disk_usage_mapping,
        "net-io":net_io_mapping,
        "net-conn":net_conn_mapping,
        "process-thread":process_thread_mapping
        }
    return type_dict[topic]