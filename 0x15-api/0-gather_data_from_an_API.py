!#/usr/bin/python3

import requests

def get_todo_progress(employee_id):
  """
  Fetches and displays an employee's TODO list progress from a REST API (assuming JSONPlaceholder).

  Args:
      employee_id (int): The ID of the employee whose progress to retrieve.
  """

  url = f"https://jsonplaceholder.typicode.com/todos/{employee_id}"

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return

  data = response.json()

  # Extract information (assuming completed is a boolean for task status)
  # Modify logic based on your actual API response structure
  completed_tasks = sum(task["completed"] for task in data)
  total_tasks = len(data)

  employee_name = "Employee Name (Placeholder)"
  print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
  for task in data:
      if task["completed"]:
      print(f"\t{task['title']}")

# Get employee ID from user input (replace with appropriate input method if needed)
employee_id = int(input("Enter employee ID: "))

get_todo_progress(employee_id)
