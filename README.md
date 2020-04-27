# Rate limiting using Python and Redis

This repository contains a Python implementation of `time-bucketed` and `GCRA` algorithms to limit requests.
For more info go to the article [Rate limiting using Python and Redis](https://dev.to/astagi/rate-limiting-using-python-and-redis-58gk)

## Setup

Configure [Redis](https://redis.io/) and make it running on the default port `6379`. Then install Python dependencies

```sh
pip install redis
```

## Run Time-bucketed

```sh
python main_tb.py
```

## Run GCRA

```sh
python main_gcra.py
```
