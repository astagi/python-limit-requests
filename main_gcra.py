import redis
from datetime import timedelta
from ratelimit import gcra


r = redis.Redis(host='localhost', port=6379, db=0)
requests = 10

for i in range(requests):
    if gcra.request_is_limited(r, 'admin', 10, timedelta(minutes=1)):
        print ('🛑 Request is limited')
    else:
        print ('✅ Request is allowed')
