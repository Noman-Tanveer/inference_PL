import requests

# Set the base URL for your FastAPI server
base_url = "http://localhost:8000"

# Define the number you want to calculate the square of
number = 25  # You can change this to any positive number you want to calculate the square of

# Send a GET request to the API
response = requests.get(f"{base_url}/square/?number={number}")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    print(f"Number: {data['number']}")
    print(f"Square: {data['square']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
