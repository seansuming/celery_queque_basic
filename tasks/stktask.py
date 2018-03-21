# -- coding: utf-8 --
__author__ = 'Sean'

from celery import Celery
from kombu import Queue
import time
from celery import Task
import sys
from conf import celeryconfig
from tasks.modules.stock.plugin_stock import PluginStock
import redis


# sys.path.append('../conf/')

app = Celery('stktask',backend='redis://:hellboy@103.235.232.114/0',broker='redis://:hellboy@103.235.232.114/0')
#app.config_from_object(celeryconfig)
# redis_config = {
#     "host": "103.235.232.114",
#     "port": 6379,
#     "pass":"hellboy"
# }

class CallbackTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print "----%s is done" % task_id

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print "----%s is failure" % task_id
        # pass

@app.task(base=CallbackTask)
def stock(t,c):
    stk=PluginStock()
    stk.set_param(t,c)
    result= stk.anyl_dadan_zhanbi()
    print result
    if result and (not len(result)==0):
        r = redis.Redis(host='103.235.232.114', port=6379, decode_responses=True,password='hellboy')
        r.lpush(t,c)

# @app.task(base=CallbackTask)
# def multiply(x,y):
#     return x * y