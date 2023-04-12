import requests
import socket
import tkinter as tk

# URLs to test the internet connection
urls = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.amazon.com"
]

# Function to get private IP address
def get_private_ip():
    return socket.gethostbyname(socket.gethostname())

# Function to get public IP address
def get_public_ip():
    response = requests.get("https://api.ipify.org")
    return response.text

# Function to test the internet connection and update the GUI label
def test_connection():
    results = []
    for url in urls:
        try:
            # Send a GET request to the URL
            response = requests.get(url)

            # Check for additional status codes
            if response.status_code == 200:
                results.append(f"Internet is connected - {url}")
            elif response.status_code == 204:
                results.append(f"No content - {url}")
            elif response.status_code == 404:
                results.append(f"Page not found - {url}")
            else:
                results.append(f"Unexpected status code {response.status_code} - {url}")
        except:
            results.append(f"Internet connection failed - {url}")

    # Update the GUI label with the results
    result_label.config(text="\n".join(results))

    # Update the IP address labels
    private_ip_label.config(text=f"Private IP: {get_private_ip()}")
    public_ip_label.config(text=f"Public IP: {get_public_ip()}")

# Create the GUI window
window = tk.Tk()
window.title("Internet Connection Test")
window.configure(bg="Black")
window.geometry("400x250")


# Create the GUI labels
label_test = tk.Label(window, text="Internet Testing",font=("Arial", 16,"bold"), bg=window["bg"], highlightthickness=0, highlightbackground=window["bg"],fg="Orange")
label_test.pack(pady=20)
result_label = tk.Label(window, text="",font=("Arial", 11,"bold"),bg=window["bg"], highlightthickness=0, highlightbackground=window["bg"],fg="light slate blue")
result_label.pack(pady=10)
private_ip_label = tk.Label(window, text="",font=("Arial", 11,"bold"),bg=window["bg"], highlightthickness=0, highlightbackground=window["bg"],fg="lime green")
private_ip_label.pack()
public_ip_label = tk.Label(window, text="",font=("Arial", 11,"bold"),bg=window["bg"], highlightthickness=0, highlightbackground=window["bg"],fg="lime green")
public_ip_label.pack()

# Create the GUI button
test_button = tk.Button(window, text="Test Connection", command=test_connection,bg="red")
test_button.pack(pady=10)

# Run the GUI window
window.mainloop()
