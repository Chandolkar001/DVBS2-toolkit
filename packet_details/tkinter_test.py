# from tkinter import *
# root = Tk() 							# Create the root (base) window 
# w = Label(root, text="Hello, world!") 	# Create a label with words
# w.pack() 								# Put the label into the window
# root.mainloop() 	

""""""

# import tkinter as tk

# # Create a temporary Tkinter window
# root = tk.Tk()

# # Get the maximum screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Close the temporary window (optional)
# root.destroy()

# print(f"Maximum Screen Size: {screen_width} x {screen_height}")

# # Use these values to set the size of your window or for other purposes

""""""

# import tkinter as tk


# class Application(tk.Frame):

#     def __init__(self, root=None):
#         tk.Frame.__init__(self, root)
#         self.grid()
#         self.createWidgets()

#     def createWidgets(self):
#         self.medialLabel = tk.Label(self, text='Hello World')
#         self.medialLabel.config(bg="#00ffff")
#         self.medialLabel.grid()
#         self.quitButton = tk.Button(self, text='Quit', command=self.quit)
#         self.quitButton.grid()


# app = Application()
# # app._root.title('Sample application')
# app.mainloop()

""""""
# import tkinter as tk

# # Create the main Tkinter window
# root = tk.Tk()
# root.title("Frame Example")

# # Create a frame with size and border
# frame = tk.Frame(root, width=200, height=100, bd=5, relief="solid", padx=10, pady=10, borderwidth=2)
# # Set width, height, bd (borderwidth), relief (border style)
# frame.pack()

# # Add widgets to the frame
# # label_in_frame = tk.Label(frame, text="This label is in the frame")
# # label_in_frame.pack()

# # button_in_frame = tk.Button(frame, text="Click Me!")
# # button_in_frame.pack()

# # Create another frame with a different background color and border
# colored_frame = tk.Frame(root, bg="lightblue", width=200, height=100, bd=2, relief="solid", padx=10, pady=10)
# # Set width, height, bd (borderwidth), relief (border style), and bg (background color)
# colored_frame.pack()
# root.resizable(False, False)

# # Add widgets to the colored frame
# # label_in_colored_frame = tk.Label(colored_frame, text="This label is in the colored frame")
# # label_in_colored_frame.pack()

# # button_in_colored_frame = tk.Button(colored_frame, text="Click Me Too!")
# # button_in_colored_frame.pack()

# # Start the Tkinter event loop
# root.mainloop()

""""""

import tkinter as tk

def on_configure(event):
    # Update the frame size when the window is resized
    frame.config(width=event.width - 20, height=event.height - 20)

# Create the main Tkinter window
root = tk.Tk()
root.title("Dynamic Frame Size Example")

# Create a frame with an initial size
frame = tk.Frame(root, width=200, height=100, padx=10, pady=10, relief="solid", borderwidth=2)
frame.pack(fill="both", expand=True)  # Fill the available space

# Add widgets to the frame
label_in_frame = tk.Label(frame, text="This label is in the frame")
label_in_frame.pack()

button_in_frame = tk.Button(frame, text="Click Me!")
button_in_frame.pack()

# Bind the on_configure function to the Configure event
root.bind("<Configure>", on_configure)

root.geometry('1600x800')

# Start the Tkinter event loop
root.mainloop()
