# -- coding: utf-8 --
__author__ = 'Sean'
from kombu import Queue
from kombu import Exchange

result_serializer = 'json'


broker_url = "redis://:hellboy@103.235.232.114/0"
# backend_url='redis://:hellboy@103.235.232.114/1'

task_queues = (
    Queue('priority_low',  exchange=Exchange('priority', type='direct'), routing_key='priority_low'),
    Queue('priority_high',  exchange=Exchange('priority', type='direct'), routing_key='priority_high'),
)

task_routes = ([
    ('tasks.add', {'queue': 'priority_low'}),
    ('tasks.multiply', {'queue': 'priority_high'}),
],)

task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}

'''
class CeleryConf():
    enable_utc = True
    timezone = 'Europe/London'
    CELERY_TRACE_APP=1
    name='stk'
    broker='redis://:hellboy@103.235.232.114/0'
    backend='redis://:hellboy@103.235.232.114/1'
'''