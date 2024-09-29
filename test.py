import requests
import os

# Base URL for the file
base_url = "http://hyperdeck-studio-hd-plus.local"
file_path = "/mounts/UNTITLED-sd1/HyperDeck_0001.mp4"

# Full URL to fetch the file
full_url = f"{base_url}{file_path}"

# Full URL to delete the file (assuming server accepts DELETE requests)
delete_url = full_url

# Directory to save the file
save_directory = "downloaded_files"

# File name extracted from the path
file_name = file_path.split("/")[-1]

# Create directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Full path to save the file
save_path = os.path.join(save_directory, file_name)

# Function to download the file
def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"File downloaded successfully: {save_path}")
            return True  # Return True if download was successful
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error occurred while downloading {url}: {e}")
        return False

# Function to delete the file from the server
def delete_file(url):
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            print(f"File deleted successfully from server: {url}")
        else:
            print(f"Failed to delete {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while deleting {url}: {e}")

# Download the file
if download_file(full_url, save_path):
    # If download is successful, delete the file from the server
    delete_file(delete_url)
