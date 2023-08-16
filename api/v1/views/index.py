#!/usr/bin/python3
"""
    Blueprint to all ALX Headache
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """returns status ok"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats')
def count_objects():
    """retrieves all objects by classes"""
    try:
        stats = {}
        classes = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
        for cls_name in classes:
            cls = storage.classes.get(cls_name)
            print(cls)
            count = storage.count(cls)
            print(count)
            stats[cls_name.lower()] = count

        # Modify the keys to convert singular to plural
        for key, val in stats.items():
            if key.endswith('y'):
                stats[key[:-1] + 'ies'] = stats.pop(key)
            else:
                stats[key + 's'] = stats.pop(key)
    except Exception as e:
        print(e)
    return jsonify(stats)