#!/usr/bin/python3


import requests
import sys


def fetch_employee_todo_progress(employee_id):
    # Fetch employee information
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)

    if employee_response.status_code != 200:
        print(f"Error fetching employee with ID {employee_id}")
        return

    employee = employee_response.json()
    employee_name = employee.get('name')

    # Fetch todos for the employee
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f"Error fetching todos for employee with ID {employee_id}")
        return

    todos = todos_response.json()

    # Calculate the number of done tasks and total tasks
    done_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todos)

    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
