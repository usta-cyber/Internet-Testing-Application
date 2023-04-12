import requests

# URLs to test the internet connection
urls = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.amazon.com"
]


# Test the internet connection for each URL
for url in urls:
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check for additional status codes
        if response.status_code == 200:
            print(f"Internet is connected - {url}")
        elif response.status_code == 204:
            print(f"No content - {url}")
        elif response.status_code == 404:
            print(f"Page not found - {url}")
        else:
            print(f"Unexpected status code {response.status_code} - {url}")
    except:
        print(f"Internet connection failed - {url}")

