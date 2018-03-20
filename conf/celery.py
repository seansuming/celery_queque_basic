# -- coding: utf-8 --
__author__ = 'Sean'

class CeleryConf():
    enable_utc = True
    timezone = 'Europe/London'
    CELERY_TRACE_APP=1
    name='stk'
    broker='redis://:hellboy@103.235.232.114/0'
    backend='redis://:hellboy@103.235.232.114/1'