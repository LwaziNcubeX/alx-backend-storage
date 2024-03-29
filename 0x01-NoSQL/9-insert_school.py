#!/usr/bin/env python3
"""Insert a new doc into the database"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new school into the database"""
    school = kwargs
    _id = mongo_collection.insert_one(school)
    return _id.inserted_id
