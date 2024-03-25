#!/usr/bin/python3
"""
Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ Fetches and prints the TODO list progress of a given employee. """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = base_url + 'users/' + str(employee_id)
    todo_url = base_url + 'todos?userId=' + str(employee_id)

    try:
        user = requests.get(user_url).json()
        user_todos = requests.get(todo_url).json()

        user_id = user.get('id')
        data = {}
        my_user = []
        for todo in user_todos:
            user_data = {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user.get('username'),
            }
            my_user.append(user_data)
            data.update({user_id: my_user})

            with open('{}.json'.format(user_id), 'w', encoding='utf-8') as f:
                json_data = json.dumps(data)
                f.write(json_data)

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
