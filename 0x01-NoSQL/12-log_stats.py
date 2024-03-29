#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    prints some stats about Nginx
    :return:
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_docs = collection.count_documents({})
    total_get = collection.count_documents({"method": "GET"})
    total_post = collection.count_documents({"method": "POST"})
    total_put = collection.count_documents({"method": "PUT"})
    total_patch = collection.count_documents({"method": "PATCH"})
    total_delete = collection.count_documents({"method": "DELETE"})
    total_status = collection.count_documents({"path": "/status"})

    print(f"{total_docs} logs\n"
          f"Methods:\n"
          f"\tmethod GET: {total_get}\n"
          f"\tmethod POST: {total_post}\n"
          f"\tmethod PUT: {total_put}\n"
          f"\tmethod PATCH: {total_patch}\n"
          f"\tmethod DELETE: {total_delete}\n"
          f"{total_status} status check")


if __name__ == "__main__":
    log_stats()
