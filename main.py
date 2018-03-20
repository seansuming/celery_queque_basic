# -- coding: utf-8 --
__author__ = 'Sean'
from celery import Celery
from tasks.stk_today_anyl_task import AnylTask



if __name__ == '__main__':
    app=Celery('tasks',broker='redis://:hellboy@103.235.232.114/0',backend='redis://:hellboy@103.235.232.114/1')
    # app.config_from_object(CeleryConf)
    print app.conf.table(with_defaults=False, censored=True)
    app.register_task(AnylTask)
    app.worker_main()