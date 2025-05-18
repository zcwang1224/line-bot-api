from enum import Enum

from constant import Constant

class RedisKey(Enum):
    USER_INFO = f"{Constant.REDIS_KEY_PREFIX}:USER_INFO"