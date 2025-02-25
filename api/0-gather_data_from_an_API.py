#!/user/bin/python3
"""
Script to fetch employee TODO list progress using a REST API.
"""
import requests
import sys

def fetch_todo_list(imployee_id):
   """Fetch and diplay TODO list progress for agiven employee
   ID."""

   #Base API URL
   base_url =  "https://jsonplaceholder.typicode.com"

   #Fetch employee details
   user_url = f"{base_url}/users/{employee_id}"

   user_response = requests.get(user_url)



if __name__ = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list(employee_id)

    
    except ValueError:
        print("Error: Employee Id must be integer")
        sys.exist(1)
