cd ../tasks
celery -A stktask worker -Q priority_high --concurrency=4 -l info -E -n worker1
#celery -A stktask worker -Q priority_high,priority_low --concurrency=4 -l info -E -n worker2