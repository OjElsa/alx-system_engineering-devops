#!/usr/bin/python3
"""Extending your Python script to export data in the CSV format. """

import argparse
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ Fetches and prints the TODO list progress of a given employee. """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f"{base_url}users/{employee_id}"
    todo_url = f"{base_url}todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_id = user_data.get('id')
        employee_name = user_data.get('username')

        csv_file = f"{employee_id}.csv"

        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(["USER_ID",
                            "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            task_count = 0
            for task in todo_data:
                writer.writerow([employee_id, employee_name,
                                task.get('completed'), task.get('title')])
                task_count += 1

        print(f"CSV file '{csv_file}' has been created.")
        status = 'OK' if task_count == len(todo_data) else 'Incorrect'
        print(f"Number of tasks in CSV: {status}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export data in CSV format.")
    parser.add_argument("employee_id", type=int, help="Employee ID")
    args = parser.parse_args()

    get_employee_todo_progress(args.employee_id)
