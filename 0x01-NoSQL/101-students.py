#!/usr/bin/env python3
"""
returns all students sorted by average score:
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average
    :param mongo_collection:
    :return:
    """
    students = mongo_collection['students'].find().sort('average_score')
    return students
