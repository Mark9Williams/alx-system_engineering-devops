#!/usr/bin/python3
"""
A script that fetches an employee's TODO list progress using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if an employee ID is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line arguments
    employee_id = sys.argv[1]

    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data to get the employee's name
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todo list for the employee
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    if todos_response.status_code != 200:
        print("TODOs not found")
        sys.exit(1)

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]

    # Print the progress of the employee's todo list
    print(f"Employee {employee_name} is done with tasks("
          f"{len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"    {task.get('title')}")
