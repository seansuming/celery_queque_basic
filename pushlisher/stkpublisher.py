from tasks import stktask
# from tasks.stktask import multiply
import time
# import redis
import tushare as ts

if __name__ == '__main__':
    d=ts.get_stock_basics()
    codes = d.index
    j=1
    for i in codes:
        j+=1
        print j
        # res=add.delay(i, 0)
        # time.sleep(1)
        # print res.ready()
        today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        res=stktask.stock.delay(today,i,400,0.30)
        # time.sleep(1)
        # print res.get(1)
    #

