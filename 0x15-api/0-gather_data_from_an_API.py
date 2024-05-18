!#/usr/bin/python3

import requests

def get_todo_progress(employee_id):
    url = f"YOUR_API_URL/employees/{employee_id}/todo"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return

    data = response.json()

  
  employee_name = data.get("name")
  completed_tasks = data.get("completed_tasks", 0)
  total_tasks = data.get("total_tasks", 0)

  # Display progress in the required format
  print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
  for task in data.get("completed_tasks_list", []):
    print(f"\t{task['title']}")

# Get employee ID from user input (replace with appropriate input method if needed)
employee_id = int(input("Enter employee ID: "))

get_todo_progress(employee_id)

