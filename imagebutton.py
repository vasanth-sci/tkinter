# Import Module
from tkinter import *

# Create Object
root = Tk()

# Add Title
root.title('On/Off Switch!')

# Add Geometry
root.geometry("800x800")

# Keep track of the button state on/off
#global is_on
is_on = True

# Create Label
my_label = Label(root, 
	text = "The Switch Is On!", 
	fg = "green", 
	font = ("Helvetica", 32))

my_label.pack(pady = 20)

# Define our switch function
def switch():
    global is_on

    # Toggle the switch state
    is_on = not is_on

    # Update button image and label text based on the switch state
    if is_on:
        on_button.config(image=on)
        my_label.config(text="The Switch is On", fg="green")
    else:
        on_button.config(image=off)
        my_label.config(text="The Switch is Off", fg="grey")
# Define Our Images
on = PhotoImage(file = "on1.png")
off = PhotoImage(file = "off1.png")

# Create A Button
on_button = Button(root, image = on, bd = 0,
				command = switch)
on_button.pack(pady = 50)

# Execute Tkinter

root.mainloop()