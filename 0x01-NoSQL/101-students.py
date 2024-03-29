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
    pipeline = [
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    students = mongo_collection.aggregate(pipeline)
    return students
