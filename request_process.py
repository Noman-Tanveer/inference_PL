import requests

# Replace with the URL of your FastAPI server
api_url = "http://localhost:8000/"  # Replace with your actual URL

def yolo_request():
    # Load an image as bytes (you can read an image file using open() in binary mode)
    with open("resources/image1-1.png", "rb") as image_file:
        image_bytes = image_file.read()

    # Send a POST request to the process-image endpoint
    response = requests.get(api_url+"detect/", files={"image_bytes": ("resources/maxresdefault.jpg", image_bytes)})

    # Check the response
    if response.status_code == 200:
        # The image processing was successful
        with open("processed_image.jpg", "wb") as processed_image_file:
            processed_image_file.write(response.content)
    else:
        # Handle the response based on your application's requirements
        print("Image processing failed:", response.status_code)

def diffusion_request():
    # Send a POST request to the generate-image endpoint
    response = requests.post(api_url+"generate-image/", json={"text": "A photo of a cat"})

    # Check the response
    if response.status_code == 200:
        # The image generation was successful
        with open("generated_image.jpg", "wb") as generated_image_file:
            generated_image_file.write(response.content)
    else:
        # Handle the response based on your application's requirements
        print("Image generation failed:", response.status_code)

if __name__ == "__main__":
    yolo_request()
    # diffusion_request()
