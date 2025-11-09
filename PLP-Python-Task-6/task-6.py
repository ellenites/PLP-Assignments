# Ubuntu-Inspired Image Fetcher
# "I am because we are"

import os
import requests
from urllib.parse import urlparse
import sys

# Step 1: Prompt the user for an image URL
image_url = input("Enter the image URL: ").strip()

# Step 2: Create directory for fetched images
folder_name = "Fetched_Images"
os.makedirs(folder_name, exist_ok=True)

# Step 3: Extract filename from URL or generate one
parsed_url = urlparse(image_url)
filename = os.path.basename(parsed_url.path)
if not filename:  # If URL doesn't end with a filename
    filename = "downloaded_image.jpg"

# Full path to save the image
file_path = os.path.join(folder_name, filename)

# Step 4: Fetch the image and save it
try:
    response = requests.get(image_url, timeout=10)
    response.raise_for_status()  # Raises HTTPError for bad responses

    # Save image in binary mode
    with open(file_path, 'wb') as f:
        f.write(response.content)
    
    print(f"Image successfully downloaded and saved as: {file_path}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("Connection error: Unable to reach the server.")
except requests.exceptions.Timeout:
    print("Timeout error: The server took too long to respond.")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
except Exception as e:
    print(f"Unexpected error: {e}")
