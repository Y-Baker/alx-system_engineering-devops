#!/usr/bin/python3
"""New Module for REST API Task"""

import json
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    users = requests.get(f"{URL}/users/").json()
    with open('todo_all_employees.json', 'w', newline='') as f:
        data = {user.get('id'): [{"username": user.get('username'), "task": task.get('title'), "completed": task.get('completed')}
                          for task in requests.get(f'{URL}/todos', params={"userId": user.get('id')}).json()]
                          for user in users}
        json.dump(data, f)
