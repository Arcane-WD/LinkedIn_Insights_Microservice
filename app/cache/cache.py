import os
from redis.asyncio import Redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)
