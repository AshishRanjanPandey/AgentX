import requests
import os

def fetch_random_image(save_path="temp/cover.png"):
    url = "https://picsum.photos/800/600"

    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(response.content)
        return save_path
    else:
        raise Exception("Failed to fetch image")
