import tkinter as tk
import subprocess

class PingTestApp:
    def __init__(self, master):
        self.master = master
        master.title("Ping Test")
        master.configure(bg="Black")
        master.geometry("250x250")

        # Create widgets
        self.newlabel=tk.Label(master, text="Ping Testing",font=("Arial", 16,"bold"), bg=master["bg"], highlightthickness=0, highlightbackground=master["bg"],fg='Red')
        self.host_label = tk.Label(master, text="Host:",font=("Arial", 14,"bold"), bg=master["bg"], highlightthickness=0, highlightbackground=master["bg"],fg="Green")
        self.host_entry = tk.Entry(master,font=("Arial", 12), fg="black")
        self.ping_button = tk.Button(master, text="Ping", command=self.ping,font=("Arial", 12), fg="black",bg="Yellow")

        self.result_label = tk.Label(master, text="",font=("Arial", 16,"bold"), bg=master["bg"], highlightthickness=0, highlightbackground=master["bg"],fg='orange')
       # self.result_label.config(font=("Arial", 12), fg="black")

        # Place widgets
        self.newlabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.host_label.grid(row=1, column=0, padx=5, pady=5)
        self.host_entry.grid(row=1, column=1, padx=5, pady=5)
        self.ping_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def ping(self):
        host = self.host_entry.get()

        # Run the ping command
        try:
            output = subprocess.check_output(["ping", "-n", "1", host])
            output_str = output.decode("utf-8")
            if "Reply from" in output_str:
                self.result_label.config(text=f"{host} is up!")
            else:
                self.result_label.config(text=f"{host} is down!")
        except subprocess.CalledProcessError:
            self.result_label.config(text=f"{host} is down!")

# Create the GUI
root = tk.Tk()
app = PingTestApp(root)
root.mainloop()
