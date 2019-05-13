"""
main_test.py

PyTest for main.py
Very simple indeed!
"""

import requests
import json

def test_get():
    result = requests.get('http://localhost:8888')
    print (result)
    assert result.status_code == 200
    assert result.text
    data = json.loads(result.text)
    assert isinstance(data['hostname'], str)
    assert isinstance(data['uid'], int)
    print (data)
