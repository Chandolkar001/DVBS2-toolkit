import tkinter as tk
import random
import string
from lorem_text import lorem

def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)
    root.geometry(screen_size)

def escape(event):
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
        root.geometry(screen_size)

def update_text():
    new_text = lorem.sentence()
    summary.delete("1.0", tk.END)
    summary.insert(tk.END, new_text)
    summary.tag_configure("bold", font=("Ubuntu", 11 ,"bold"))
    summary.tag_add("bold", "1.0", "end")

    new_text = lorem.sentence()
    details.delete("1.0", tk.END)
    details.insert(tk.END, new_text)
    details.tag_configure("bold", font=("Ubuntu", 11 ,"bold"))
    details.tag_add("bold", "1.0", "end")

    root.after(500, update_text)


# def on_configure(event):
#     menu_section.config(width=event.width * 0.2, height=event.height)  # Subtracting borderwidth
#     media_section.config(width=event.width * 0.4, height=event.height * 0.5)  # Subtracting borderwidth
#     analyzer_section.config(width=event.width * 0.4, height=event.height * 0.5)  # Subtracting borderwidth

# screen_size = '1600x800+50+50'
screen_size = '1600x800'
min_width, min_height = 1600, 800

root = tk.Tk()
root.title("Packet Analyzer")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.minsize(min_width, min_height)

root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', escape)

root.geometry(screen_size)
toggle_fullscreen() 

# root.bind("<Configure>", on_configure)

for i in range(10):
    root.grid_columnconfigure(i, weight=1)

for i in range(2):
    root.grid_rowconfigure(i, weight=1)

# --- Frames --- #
menu_section = tk.Frame(root, bg="#1d1927", padx=10, pady=10, relief="solid")
menu_section.grid(row=0, column=0,rowspan=2,columnspan=1, sticky="nsew")

media_section = tk.Frame(root, bg="#241F31", relief="solid")
media_section.grid(row=0, column=1,rowspan=1,columnspan=9, sticky="nsew")

analyzer_section = tk.Frame(root, bg="#241F31", relief="solid")
analyzer_section.grid(row=1, column=1,rowspan=1,columnspan=9, sticky="nsew")

media_section.grid_columnconfigure(0, weight=1)
media_section.grid_rowconfigure(0, weight=1)

for i in range(2):
    analyzer_section.grid_columnconfigure(i, weight=1)
analyzer_section.grid_rowconfigure(0, weight=1)


# --- Widgets --- #

label_in_frame = tk.Label(menu_section, text="menu_section", font=("Ubuntu"))
label_in_frame.pack()

text_in_media_section = tk.Text(media_section, bd=-1, bg="#3a3546", fg="#2EC27E")
text_in_media_section.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
new_text = "Media"
text_in_media_section.insert(tk.END, new_text)

# summary = tk.Label(analyzer_section, bg="#434343", fg="#d6d6d6", text="summary", font=("Ubuntu"))
# summary.grid(row=0, column=0, sticky="nsew", pady=10,padx=10)
# details = tk.Label(analyzer_section,bg="#434343", fg="#d6d6d6",text="details", font=("Ubuntu"))
# details.grid(row=0, column=1, sticky="nsew", pady=10,padx=10)

summary = tk.Text(analyzer_section, bd=-1, bg="#3a3546", fg="#2EC27E")
summary.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

details = tk.Text(analyzer_section, bd=-1, background="#3a3546", fg="#2EC27E")
details.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

update_text()

root.mainloop()

"""
    Features:
        Full screen mode initially,
        Minimum size set to 1600x800
        frames adjustable to window size

"""

"""
    Bugs:
        When escape is hit for the first time the title bar is not visible.
        root.geometry(screen_size), Commented as after pressing escape it should only exit fullscreen mode
        and not resize the screen.

        Solved by conditional check
"""

"""
https://www.plus2net.com/python/tkinter-colors.php
"""