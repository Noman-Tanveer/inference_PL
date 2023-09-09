import requests

# Replace with the URL of your FastAPI server
api_url = "http://localhost:8000/detect/"  # Replace with your actual URL

# Load an image as bytes (you can read an image file using open() in binary mode)
with open("resources/maxresdefault.jpg", "rb") as image_file:
    image_bytes = image_file.read()

# Send a POST request to the process-image endpoint
response = requests.get(api_url, files={"image_bytes": ("resources/maxresdefault.jpg", image_bytes)})

# Check the response
if response.status_code == 200:
    # The image processing was successful
    with open("processed_image.jpg", "wb") as processed_image_file:
        processed_image_file.write(response.content)
else:
    # Handle the response based on your application's requirements
    print("Image processing failed:", response.status_code)
