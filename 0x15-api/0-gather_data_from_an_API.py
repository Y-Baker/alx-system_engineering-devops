#!/usr/bin/python3
"""New Module for REST API Task"""

import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(argv) > 1:
        id = int(argv[1])
        url_user = f"{URL}/users/{id}"
        emp_name = requests.get(url=url_user).json().get('name')
        tasks_resp = requests.get(f"{URL}/todos/").json()
        tasks = list(filter(lambda _: _.get('userId') == id, tasks_resp))
        tasks_complete = list(filter(lambda _: _.get('completed'), tasks))

        print(f"Employee {emp_name} is done with tasks\
({len(tasks_complete)}/{len(tasks)}):")

        for task in tasks_complete:
            print(f"\t {task.get('title')}")
