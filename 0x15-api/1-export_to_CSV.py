#!/usr/bin/python3
"""Extending your Python script to export data in the CSV format. """


import requests
import sys
import csv


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

        employee_name = user_data.get('username')

        csv_file = f"{employee_id}.csv"

        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(["USER_ID",
                            "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in todo_data:
                writer.writerow([employee_id, employee_name,
                                task.get('completed'), task.get('title')])

        print(f"CSV file '{csv_file}' has been created.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
