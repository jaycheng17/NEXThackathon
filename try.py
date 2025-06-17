import requests
from PIL import Image

# Image URL
url = "https://i.pinimg.com/236x/ba/c7/12/bac7127211c77188ea44b7e5042425ad.jpg"

# Send HTTP GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the image to a file
    with open("downloaded_image.jpg", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully.")
else:
    print(f"Failed to download image. Status code: {response.status_code}")




# Open the .jpg image
image = Image.open("downloaded_image.jpg")

# Save the image as .jpeg
image.save("image_converted.jpeg", "JPEG")


