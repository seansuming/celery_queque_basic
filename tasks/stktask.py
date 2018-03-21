# -- coding: utf-8 --
__author__ = 'Sean'
from celery import Celery
from kombu import Queue
import time
from celery import Task
import sys

sys.path.append('../conf/')

app = Celery('tasks',backend='redis://:hellboy@103.235.232.114/0',broker='redis://:hellboy@103.235.232.114/0')
# app.config_from_object('celeryconfig')

class CallbackTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print "----%s is done" % task_id

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print "----%s is failure" % task_id
        # pass

@app.task(base=CallbackTask)
def add(x, y):
    return x + y


@app.task(base=CallbackTask)
def multiply(x,y):
    return x * y