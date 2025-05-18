#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import redis


class redisClient(object):

    #def __init__(self, url):
    #    pool = redis.ConnectionPool.from_url(url, decode_components=True)
    #    self._redis = redis.Redis(connection_pool=pool)

    def connection(self, url):
        try:
            #pool = redis.ConnectionPool.from_url(url, decode_components=True)
            pool = redis.ConnectionPool.from_url(url, decode_responses=False)
            self.op = redis.Redis(connection_pool=pool)
            self.op.ping()
            return 0
        except redis.exceptions.TimeoutError:
            return -1

    def keys(self, key=None):
        if key == None:
            return self.op.keys()
        return self.op.keys(key)

    def get(self, key):
        return self.op.get(key)


    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        return self.op.set(name, value, ex, px, nx, xx)


    def scan(self, key):
        cursor, keys = self.op.scan(match=key)
        return keys


    def deleteAllKeys(self):
        self.op.flushdb()


    def deleteByKeys(self, keys):
        for key in keys:
            self.op.delete(key)


    def delete(self, key):
        return self.op.delete(key)


    def zadd(self, key, value):
        return self.op.zadd(key, value)


    def zrange(self, key):
        return self.op.zrange(key, 0, -1, withscores=True)


    def zrevrank(self, name, value):
        return self.op.zrevrank(name, value)


    def zremrangebyscore(self, name, min, max):
        return self.op.zremrangebyscore(name, min, max)


    def expire(self, key, time):
        return self.op.expire(key, time)


    def getExpireTime(self, key):
        return self.op.ttl(key)


    def exists(self, key):
        return self.op.exists(key)


    def publish(self, key, value):
        return self.op.publish(key, value)

    def sort(self, key, alpha=True):
        return self.op.sort(key, alpha=alpha)

    def getPubsubChs(self, key='*'):
        return self.op.pubsub_channels(key)

redis_client = redisClient()

if __name__ == '__main__':
    redis_client.connection("redis://localhost")
