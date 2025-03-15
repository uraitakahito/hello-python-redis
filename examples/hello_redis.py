import redis

# > redis-py 3.0 drops support for the legacy "Redis" client class. "StrictRedis" has been renamed to "Redis" and an alias named "StrictRedis" is provided so that users previously using "StrictRedis" can continue to run unchanged.
# https://stackoverflow.com/questions/19021765/redis-py-whats-the-difference-between-strictredis-and-redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Add a value 'moge' with the key 'hoge'
r.set("hoge", "moge", ex=10)

# Retrieve and display the added value
hoge = r.get("hoge")
print(hoge.decode())

# % uv run python examples/hello_redis.py
# moge
#
# (After 10 seconds)
#
# % hello-python-redis% redis-cli -h localhost
# localhost:6379> GET hoge
# (nil)
