#!/usr/bin/python3
"""New Module for REST API Task"""

import json
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(argv) > 1:
        id = int(argv[1])
        url_user = f"{URL}/users/{id}"
        emp_name = requests.get(url=url_user).json().get('username')
        tasks_resp = requests.get(f"{URL}/todos/").json()
        tasks = list(filter(lambda _: _.get('userId') == id, tasks_resp))

        with open(f'{id}.json', "w", newline='') as f:
            data = {id: [{"task": task.get('title'),
                          "completed": task.get('completed'),
                          "username": emp_name} for task in tasks]}
            print(type(data))
            print(data)
            json.dump(data, f)
