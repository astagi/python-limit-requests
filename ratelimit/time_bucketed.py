import time
import random
from datetime import timedelta
from redis import Redis


def request_is_limited(r: Redis, key: str, limit: int, period: timedelta):
    #TTL returns -2 if the key does not exist and -1 if the key has no TTL.
    #Reference: https://redis.io/commands/ttl
    if int(r.ttl(key)) < 0:
        #Creates a key and adds an expire atomically.
        r.setex(key, int(period.total_seconds()), limit)
    if r.exists(key):
        #DECR creates a key with the value -1 if the key does not yet exist.
        #Checks if this happend because there is a race condition.
        #Reference: https://redis.io/commands/decr
        if int(r.decr(key)) >= 0:
            return False
    #Prevents an unnecessarily high number of database accesses while the
    #request is limited.
    time.sleep(random.random()/limit)
    return True
