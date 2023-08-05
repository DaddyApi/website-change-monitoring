import requests
import hashlib
import time

# Define the URL of the webpage you want to monitor
url_to_monitor = "https://example.com"

# Define your API endpoint and headers
api_url = "https://api.rapidapi.com/fetch-simple"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Host": "<your-api-host>",
    "X-RapidAPI-Key": "<your-api-key>"
}

# Function to fetch webpage content using our API
def fetch_content(url):
    payload = {"url": url}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()["content"]

# Function to generate a hash of the webpage content
def get_content_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

# Monitor the webpage for changes
def monitor_webpage(url):
    print(f"Starting to monitor {url}")
    last_hash = get_content_hash(fetch_content(url))

    while True:
        time.sleep(60)  # wait for 60 seconds
        current_content = fetch_content(url)
        current_hash = get_content_hash(current_content)
        if current_hash != last_hash:
            print(f"Change detected on {url}")
            last_hash = current_hash

# Start monitoring
monitor_webpage(url_to_monitor)
