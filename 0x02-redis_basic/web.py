#!/usr/bin/env python3
"""
Redis web app count tracker
"""
from functools import wraps
import redis
import requests
from typing import Callable

redis_client: redis.StrictRedis = redis.StrictRedis(host='localhost', port=6379, db=0)


def track_url_access(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to track URL access count.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """Wrapper function to track URL access count."""
        redis_client.incr(f"count:{url}")
        return func(url)
    return wrapper


def cache_page(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to cache page content.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """Wrapper function to cache page content."""
        cached_result = redis_client.get(f"cache:{url}")
        if cached_result:
            return cached_result.decode('utf-8')
        else:
            page_content = func(url)
            redis_client.setex(f"cache:{url}", 10, page_content)
            return page_content
    return wrapper


@cache_page
@track_url_access
def get_page(url: str) -> str:
    """
    Get page content from the given URL.
    """
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)



"""
if __name__ == "__main__":
    # Test the get_page function
    test_url = "http://slowwly.robertomurray.co.uk/"
    print(get_page(test_url))
    time.sleep(2)  # Wait to ensure caching expires
    print(get_page(test_url))
"""
