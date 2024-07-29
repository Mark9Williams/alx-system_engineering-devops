#!/usr/bin/python3
"""
A script that fetches an employee's TODO lisst and exports
data in the JSON format.
"""

import json
import requests

# Fetch all users
users_url = "https://jsonplaceholder.typicode.com/users"
users_response = requests.get(users_url)
users = users_response.json()

# Dictionary to hold data for all employees
all_tasks = {}

# Fetch all TODOs
todos_url = "https://jsonplaceholder.typicode.com/todos"
todos_response = requests.get(todos_url)
todos = todos_response.json()

# Structure data in the required format
for user in users:
    user_id = str(user['id'])
    username = user['username']

    # Filter todos for the current user
    user_todos = [todo for todo in todos if todo['userId'] == user['id']]

    # Format the data as required
    all_tasks[user_id] = [
        {
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        }
        for todo in user_todos
    ]

# Write the data to a JSON file
with open('todo_all_employees.json', mode='w') as jsonfile:
    json.dump(all_tasks, jsonfile)
