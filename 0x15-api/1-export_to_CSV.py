#!/usr/bin/python3
"""New Module for REST API Task"""

import requests
import csv
from sys import argv

URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(argv) > 1:
        id = int(argv[1])
        url_user = f"{URL}/users/{id}"
        emp_name = requests.get(url=url_user).json().get('username')
        tasks_resp = requests.get(f"{URL}/todos/").json()
        tasks = list(filter(lambda _: _.get('userId') == id, tasks_resp))

    with open(f'{id}.csv', 'w', newline="") as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([id, emp_name,
                             task.get('completed'),
                             task.get('title')])
