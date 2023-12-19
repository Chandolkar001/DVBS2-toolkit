import subprocess
import tkinter as tk
from tkinter import scrolledtext

def capture_packets():
    interface = "wlo1"  # Replace with your network interface
    command = ["tshark", "-i", interface, "-n"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    for line in process.stdout:
        # Process each line of captured packet data
        # You can customize this part to extract and display specific information
        packet_info_text.insert(tk.END, line)
        packet_info_text.yview(tk.END)

# Create the main application window
app = tk.Tk()
app.title("Packet Capture and Display")

# Create a button to start packet capture
start_button = tk.Button(app, text="Start Capture", command=capture_packets)
start_button.pack(pady=10)

# Create a scrolled text widget to display packet information
packet_info_text = scrolledtext.ScrolledText(app, width=80, height=20)
packet_info_text.pack(padx=10, pady=10)

# Run the Tkinter main loop
app.mainloop()
