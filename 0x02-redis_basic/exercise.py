#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import typing
import uuid
from functools import wraps
from typing import Union
import redis


def count_calls(method: typing.Callable) -> typing.Callable:
    """
    Decorator to count how many times a method call is made
    :param method:
    :return:
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = f"{self.__class__.__qualname__}.{method.__name__}"
        r = redis.Redis()
        r.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    def __init__(self):
        """
        Initializes Redis Cache object
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate and set a unique key for each data
        :param data:
        :return:
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: typing.Optional[typing.Callable] = None
            ) -> Union[str, bytes, int, None]:
        """
        get data from Redis cache
        :param key:
        :param fn:
        :return: value or None
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str,
                fn: typing.Optional[typing.Callable] = None) -> str:
        """
        get data from Redis as a string in type
        :param key:
        :param fn:
        :return:
        """
        value = self.get(key, fn)
        if isinstance(value, bytes):
            return value.decode('utf-8')
        return str(value) if value is not None else ""

    def get_int(self, key: str,
                fn: typing.Optional[typing.Callable] = None) -> int:
        """
        get data from Redis as an int in type
        :param key:
        :param fn:
        :return:
        """
        value = self.get(key, fn)
        return int(value) if value is not None else 0


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
