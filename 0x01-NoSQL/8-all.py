#!/usr/bin/env python3
"""
Mongodb: List all documents in Python
"""


def list_all(mongo_collection):
    """
    List all documents in mongodb collection
    :param mongo_collection:
    :return:
    """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents


if __name__ == "__main__":
    list_all(mongo_collection="")
