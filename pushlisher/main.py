# -- coding: utf-8 --
__author__ = 'Sean'

from celery import Celery
from conf.celeryconfig import CeleryConf
from tasks.stk_today_anyl_task import AnylTask



if __name__ == '__main__':
    app=Celery('tasks',broker='redis://:hellboy@103.235.232.114/0',backend='redis://:hellboy@103.235.232.114/1')
    # app.config_from_object(CeleryConf)
    app.register_task(task=AnylTask)
    res=AnylTask.delay()
    res.ready()