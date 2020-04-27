import redis
from datetime import timedelta
from ratelimit import time_bucketed


r = redis.Redis(host='localhost', port=6379, db=0)
requests = 25

for i in range(requests):
    if time_bucketed.request_is_limited(r, 'admin', 20, timedelta(seconds=30)):
        print ('🛑 Request is limited')
    else:
        print ('✅ Request is allowed')
