#!/usr/bin/env python3
"""
returns the list of school having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    :param mongo_collection:
    :param topic:
    :return:
    """
    query = {"topics": topic}
    result = mongo_collection.find(query)
    return result
