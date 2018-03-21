from tasks.stktask import add
from tasks.stktask import multiply
import time


# res=dict()
for i in xrange(50):
    res=add.delay(2, 2)
    time.sleep(1)
    print res.ready()

    res=multiply.delay(10,10)
    time.sleep(1)
    print res.ready()

