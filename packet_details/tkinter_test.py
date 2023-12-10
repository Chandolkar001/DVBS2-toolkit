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

# import tkinter as tk

# def on_configure(event):
#     # Update the frame size when the window is resized
#     frame.config(width=event.width - 20, height=event.height - 20)

# # Create the main Tkinter window
# root = tk.Tk()
# root.title("Dynamic Frame Size Example")

# # Create a frame with an initial size
# frame = tk.Frame(root, width=200, height=100, padx=10, pady=10, relief="solid", borderwidth=2)
# frame.pack(fill="both", expand=True)  # Fill the available space

# # Add widgets to the frame
# label_in_frame = tk.Label(frame, text="This label is in the frame")
# label_in_frame.pack()

# button_in_frame = tk.Button(frame, text="Click Me!")
# button_in_frame.pack()

# # Bind the on_configure function to the Configure event
# root.bind("<Configure>", on_configure)

# root.geometry('1600x800')

# # Start the Tkinter event loop
# root.mainloop()

""""""

# import tkinter as tk

# root = tk.Tk()
# root.title("Grid Example")

# # Configure rows and columns to have equal weight so they share the available space equally
# for i in range(3):
#     root.grid_rowconfigure(i, weight=1)
#     root.grid_columnconfigure(i, weight=1)

# # Create frames
# frame1 = tk.Frame(root, bg="lightgreen", relief="solid", borderwidth=2)
# frame2 = tk.Frame(root, bg="lightblue", relief="solid", borderwidth=2)
# frame3 = tk.Frame(root, bg="lightcoral", relief="solid", borderwidth=2)

# # Place frames in cells
# frame1.grid(row=0, column=0,rowspan=3,columnspan=1, sticky="nsew")
# frame2.grid(row=0, column=2, sticky="nsew")
# frame3.grid(row=1, column=2, sticky="nsew")

# # Add labels or other widgets within frames if needed
# label_frame1 = tk.Label(frame1, text="Frame 1")
# label_frame1.pack()

# label_frame2 = tk.Label(frame2, text="Frame 2")
# label_frame2.pack()

# label_frame3 = tk.Label(frame3, text="Frame 3")
# label_frame3.pack()

# root.geometry("800x600")

# root.mainloop()


""""""
# import tkinter as tk
# from lorem_text import lorem

# def update_labels():
#     label1.config(text="Updated Text 1")
#     label2.config(text="Updated Text 2")

# root = tk.Tk()
# root.title("Labels with Margin Example")

# # Configure row and column weights
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(1, weight=1)

# lorem.sentence()

# # Create Labels
# label1 = tk.Label(root, text=lorem.sentence(), bg="#2e2e2e", font=("Helvetica", 12), wraplength=200)
# label1.grid(row=0, column=0, pady=10, sticky="nsew")

# label2 = tk.Label(root, text="Label 2 Lorem", bg="#2e2e2e", font=("Helvetica", 12), wraplength=200)
# label2.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")

# root.geometry("800x600")

# root.mainloop()

""""""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def display_image():
    image_path = "sample_image.png"
    img = Image.open(image_path)
    img = img.resize((300, 200))
    photo = ImageTk.PhotoImage(img)
    
    image_label.config(image=photo)
    image_label.image = photo

def display_video():
    # Replace "path/to/your/video.mp4" with the actual path to your video file
    video_path = "sample_video.mp4"
    
    # You'll need to install a video player library, such as cv2, for this to work
    import cv2
    
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    
    # Convert the frame from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Convert the frame to a PhotoImage
    photo = ImageTk.PhotoImage(Image.fromarray(frame_rgb))
    
    video_label.config(image=photo)
    video_label.image = photo

    # Update the video display periodically
    video_label.after(30, display_video)

# Create the main Tkinter window
root = tk.Tk()
root.title("Media Display Example")

# Create a label for displaying an image
image_label = tk.Label(root)
image_label.pack(pady=10)

# Create a button to trigger image display
image_button = tk.Button(root, text="Display Image", command=display_image)
image_button.pack(pady=10)

# Create a label for displaying a video
video_label = ttk.Label(root)
video_label.pack(pady=10)

# Create a button to trigger video display
video_button = tk.Button(root, text="Display Video", command=display_video)
video_button.pack(pady=10)

root.geometry("400x600")
root.mainloop()
