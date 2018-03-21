
# import sys
# sys.path.append('/root/workspace/celery_queque_basic')

from tasks.stktask import stock
# from tasks.stktask import multiply
import time
# import redis
import tushare as ts
from tasks.modules.stock.plugin_stock import PluginStock

if __name__ == '__main__':
    # d=ts.get_stock_basics()
    # codes = d.index
    # for i in codes:
    #     # res=add.delay(i, 0)
    #     # time.sleep(1)
    #     # print res.ready()
    #     today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    #     res=stock.delay(i,today)
    #     # time.sleep(1)
    #     # print res.get(1)
    # #
    stk=PluginStock()
    stk.set_param('2018-3-21','603333')
    result= stk.anyl_dadan_zhanbi()
    print result