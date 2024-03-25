#!/usr/bin/python3
"""
A Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    """ Fetches and prints the TODO list progress of a given employee. """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = base_url + 'users/' + str(employee_id)
    todo_url = base_url + 'todos?userId=' + str(employee_id)

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data.get('name')
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task.get('completed'))

        print("Employee {} is done with tasks({}/{}): ".format(
            employee_name, completed_tasks, total_tasks))

        for task in todo_data:
            if task.get('completed'):
                print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
