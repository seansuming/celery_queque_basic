from tasks.stktask import add
from tasks.stktask import multiply

res=dict()
for i in xrange(50):
    res=add.delay(2, 2)
    print res.ready()

    res=multiply.delay(10,10)
    print res.ready()

