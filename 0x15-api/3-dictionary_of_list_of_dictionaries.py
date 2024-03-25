#!/usr/bin/python3
"""
Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    try:
        all_employees = {}
        for employee_id in range(1, 11):
            base_url = 'https://jsonplaceholder.typicode.com/'
            user_url = base_url + 'users/' + str(employee_id)
            todo_url = base_url + 'todos?userId=' + str(employee_id)

            user = requests.get(user_url).json()
            user_todos = requests.get(todo_url).json()

            user_id = user.get('id')
            my_user = []
            for todo in user_todos:
                user_data = {
                        "username": user.get('username'),
                        "task": todo.get('title'),
                        "completed": todo.get('completed'),
                }
                my_user.append(user_data)
            all_employees.update({user_id: my_user})

        with open('todo_all_employees.json'.format(user_id), 'w',
                  encoding='utf-8') as f:
            json_data = json.dumps(all_employees)
            f.write(json_data)

    except Exception as e:
        print("Error:", e)
        sys.exit(1)
