from tasks.stktask import add
result=add.delay(4, 4)
result.ready()