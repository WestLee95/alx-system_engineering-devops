#!/usr/bin/python3

import requests
import sys


"""
0-gather_data_from_an_API.py

This script retrieves and displays the TODO list progress of an employee
based on their ID from a public API. It fetches user data to obtain the
employee's name and their associated tasks, displaying the number of
completed and total tasks along with the titles of the completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Parameters:
    employee_id: An integer representing the employee's ID.

Requirements:
    - requests module
"""


def fetch_employee_todo_progress(employee_id):
    try:
        # Fetch user data to get the employee's name
        user_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        user_response.raise_for_status()  # Raise an exception for HTTP errors
        user_data = user_response.json()

        employee_name = user_data.get('name', 'Unknown')

        # Fetch todo list data for the employee
        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate the number of completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = [todo for todo in todos_data if todo['completed']]
        number_of_done_tasks = len(completed_tasks)

        # Display the employee's TODO list progress
        print(
            f"Employee {employee_name} is done with tasks(
                {number_of_done_tasks} / {total_tasks}): ")

        # Display the title of each completed task
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")

if __name__ == "__main__":
    main()
