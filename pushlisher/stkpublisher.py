from tasks.stktask import add
from tasks.stktask import multiply


for i in xrange(50):
    add.delay(2, 2)
    multiply.delay(10,10)