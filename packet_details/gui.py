import tkinter as tk

def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)
    root.geometry(screen_size)

def escape(event):
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
        root.geometry(screen_size)


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

menu_section = tk.Frame(root, width=screen_width * 0.15, bg="lightgreen", relief="solid", borderwidth=2)
menu_section.pack(side="left", fill="y") 

media_section = tk.Frame(root, bg="lightcoral", relief="solid", borderwidth=2)
media_section.pack(side="top", fill="both", expand=True) 

analyzer_section = tk.Frame(root, bg="lightblue", relief="solid", borderwidth=2)
analyzer_section.pack(side="bottom", fill="both", expand=True) 

# root.bind("<Configure>", on_configure)

root.geometry(screen_size)
toggle_fullscreen() 

root.mainloop()


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