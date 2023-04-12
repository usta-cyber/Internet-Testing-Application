import requests

# The URL to test the internet connection
url = "https://www.google.com"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # If the response is successful (status code 200), print "Internet is connected"
    if response.status_code == 200:
        print("Internet is connected")
    else:
        print("Internet connection failed")
except:
    print("Internet connection failed")
