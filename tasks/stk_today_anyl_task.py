# -- coding: utf-8 --
__author__ = 'Sean'

from celery.task import Task

class AnylTask(Task):

    def run(self, to):
        return 'hello {0}'.format(to)