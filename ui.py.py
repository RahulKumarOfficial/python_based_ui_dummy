# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:57:00 2023

@author: rahul
"""


from tkinter import *
from tkcalendar import DateEntry
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x500")
root.title("Elegant UI with Icons")
def print_values():
    print("String 1:", string1.get())
    print("String 2:", string2.get())
    print("Date 1:", date1.get_date())
    print("Date 2:", date2.get_date())

# Set font and background color
font = ("Helvetica", 12)
bg_color = "#D3D3D3" # light grey
root.configure(bg=bg_color)

# Create frames for better organization
input_frame = Frame(root, bg=bg_color)
input_frame.pack(pady=20)

# Load and resize icons
icon_size = (32, 32)
string_icon = Image.open("images/string_icon.png").resize(icon_size)
string_icon = ImageTk.PhotoImage(string_icon)
calendar_icon = Image.open("images/calendar_icon.png").resize(icon_size)
calendar_icon = ImageTk.PhotoImage(calendar_icon)
submit_button = Button(root, text="Submit", font=font, command=print_values)
submit_button.pack(pady=10)


# # String inputs
Label(input_frame, image=string_icon, bg=bg_color).grid(row=0, column=0, padx=10, pady=10)
Label(input_frame, text="Sprint Name:", font=font, bg=bg_color).grid(row=0, column=1, padx=10, pady=10)
string1 = Entry(input_frame, font=font)
string1.grid(row=0, column=2)

Label(input_frame, image=string_icon, bg=bg_color).grid(row=1, column=0, padx=10, pady=10)
Label(input_frame, text="User / List of users:", font=font, bg=bg_color).grid(row=1, column=1, padx=10, pady=10)
string2 = Entry(input_frame, font=font)
string2.grid(row=1,column = 2)

# Calendar inputs
Label(input_frame, image=calendar_icon, bg=bg_color).grid(row=2,column = 0,padx = 10,pady = 10)
Label(input_frame,text="Start Date:",font = font,bg = bg_color).grid(row = 2,column = 1,padx = 10,pady = 10)
date1 = DateEntry(input_frame,font = font)
date1.grid(row = 2,column = 2)

Label(input_frame,image = calendar_icon,bg = bg_color).grid(row = 3,column = 0,padx = 10,pady = 10)
Label(input_frame,text="End Date:",font = font,bg = bg_color).grid(row = 3,column = 1,padx = 10,pady = 10)
date2 = DateEntry(input_frame,font = font)
date2.grid(row = 3,column = 2)

root.mainloop()
