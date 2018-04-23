from tasks import stktask
# from tasks.stktask import multiply
import time
# import redis
import tushare as ts
import redis


if __name__ == '__main__':
    today=time.strftime('%Y-%m-%d',time.localtime(time.time()))

    r.delete(today)
    d=ts.get_stock_basics()

    codes = d.index
    j=1
    for i in codes:
        j+=1
        print j
        # res=add.delay(i, 0)
        # time.sleep(1)
        # print res.ready()

        res=stktask.stock.delay(today,i,0,0.50)
        # time.sleep(1)
        # print res.get(1)
    #

