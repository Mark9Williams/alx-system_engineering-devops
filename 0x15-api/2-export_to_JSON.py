#!/usr/bin/python3
import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Get user information to get the username
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
user_response = requests.get(user_url)
user_data = user_response.json()
username = user_data.get('username')

# Get the todo list for the employee
todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
todos_response = requests.get(todos_url)
todos = todos_response.json()

# Prepare the data in the specified JSON format
data = {
    employee_id: [
        {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        for todo in todos
    ]
}

# Write the data to a JSON file
json_filename = f"{employee_id}.json"
with open(json_filename, mode='w') as jsonfile:
    json.dump(data, jsonfile)
