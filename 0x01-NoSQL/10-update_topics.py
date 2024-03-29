#!/usr/bin/env python3
"""
changes all topics of a school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name:
    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    name = {"name": name}
    set_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(name, set_values)
