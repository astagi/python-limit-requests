from datetime import timedelta
from redis import Redis


def request_is_limited(r: Redis, key: str, limit: int, period: timedelta):
    if r.setnx(key, limit):
        r.expire(key, int(period.total_seconds()))
    bucket_val = r.get(key)
    if bucket_val and int(bucket_val) > 0:
        r.decrby(key, 1)
        return False
    return True
