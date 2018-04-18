# -- coding: utf-8 --
__author__ = 'Sean'
import tushare as ts
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class PluginStock():
    def __init__(self):
        pass

    def set_param(self, time_start, codes,maxval=400,zhanbi=0.0):
        # d=ts.get_stock_basics()
        self._time_start = time_start
        # self._time_end = time_end
        # d=ts.get_stock_basics()
        self._maxval=maxval
        self._zhanbi=zhanbi
        if isinstance(codes,list):
            self._codes = codes
        else:
            self._codes = [codes]

    def anyl_dadan_zhanbi(self):
        matchs=[]
        j=0
        for code in self._codes:
            # if code.startswith('300'):
            #     continue
            # code_zhanbi=()
            # code_zhanbi['code']=code
            j+=1
            df=ts.get_realtime_quotes(code)
                # keys=numpy.array(df.volume.keys).tolist()
                # if not days[i] in keys:
                #     continue
            if 0 not in df.volume:
                continue
            chengjiaoliang=0
            if self._maxval<=0:
                chengjiaoliang=float(df.volume[0])
                self._maxval=int(chengjiaoliang*0.00005)
            print self._maxval
            print '-----------------------'
            # print ('%d/%d current=%s' %(j,len(self._codes),code))
            ds = ts.get_sina_dd(code=code, date=self._time_start,vol=self._maxval)
                # ds['total']=ds.price*ds.volume
                # maipantol=ds[ds.type=='买盘'].total.sum()
                # maipan1tol=ds[ds.type=='卖盘'].total.sum()
            if ds is None:
                continue
            maipantol=ds[ds.type=='买盘'].volume.sum()
            maipan1tol=ds[ds.type=='卖盘'].volume.sum()
            jinliuru=maipantol-maipan1tol

            # df= ts.get_hist_data(code=code,start=self._time_start,end=self._time_start)
            time.sleep(1)

            if jinliuru==0.0 or chengjiaoliang==0.0:
                continue
            liuruzhanbi=jinliuru/chengjiaoliang

            # p_change=(df.price-df.open[0])/df.open[0]
            # if liuruzhanbi<self._zhanbi:
            #     print liuruzhanbi
            #     continue
            # code_zhanbi['zhanbi']=liuruzhanbi
            matchs.append((code,liuruzhanbi,time.asctime(time.localtime(time.time()))))
            # print ('date=%s,code=%s,liuruzhanbi=%s' %(str(self._time_start),str(code),str(liuruzhanbi)))
                # print ('date=%s,code=%s,zhangfu=%s,jinliuru=%s' %(str(days[i]),str(self._codes[0]),str(secdayzhangfu),str(jinliuru)))
        # print matchs
        return matchs

            # for code in self._codes:
            #     print code
