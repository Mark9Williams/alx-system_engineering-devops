#!/usr/bin/python3
import csv
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

# Open a CSV file to write the data
csv_filename = f"{employee_id}.csv"
with open(csv_filename, mode='w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # Write the CSV data
    for todo in todos:
        csv_writer.writerow([employee_id, username, 
        todo.get('completed'), todo.get('title')])
