
import tkinter as tk

window = tk.Tk()

window.title("Log in")
window.geometry("1000x600")
window.resizable(False, False)
window.configure(bg="black")

# Frame
frame1 = tk.Frame(window, width=400, height=400, bg="white")
frame1.place(x=300, y=80)

# Entries
# Name
# Age
# Address
# Gender
# Username
# Password

name1 = tk.Label(frame1, text="Fullname:", fg="black", bg="white", font=("arial", 12, "italic"))
name1.place(x=20, y=20)

name2 = tk.Entry(frame1, bg="white")
name2.place(x=100, y=24)

age1 = tk.Label(frame1, text="Age:", fg="black", bg="white", font=("arial", 12, "italic"))
age1.place(x=58, y=50)

age2 = tk.Entry(frame1, bg="white")
age2.place(x=100, y=55)

place1 = tk.Label(frame1, text="Address:", fg="black", bg="white", font=("arial", 12, "italic"))
place1.place(x=25, y=80)

place2 = tk.Entry(frame1, bg="white", width=20)
place2.place(x=100, y=85)

# Gender - only one can be selected
gender = tk.StringVar(value="")

male1 = tk.Radiobutton(frame1, text="Male", variable=gender, value="Male", bg="lightblue")
male1.place(x=20, y=120)

fmale1 = tk.Radiobutton(frame1, text="Female", variable=gender, value="Female", bg="lightpink")
fmale1.place(x=80, y=120)

line = tk.Label(frame1, text="-------------------------------------------------------", fg="black", bg="white")
line.place(x=20, y=160)

Uname1 = tk.Label(frame1, text="Username:", fg="black", bg="white", font=("arial", 12, "italic"))
Uname1.place(x=20, y=190)

Uname2 = tk.Entry(frame1, bg="white")
Uname2.place(x=108, y=195)

Pword1 = tk.Label(frame1, text="Password:", fg="black", bg="white", font=("arial", 12, "italic"))
Pword1.place(x=20, y=230)

Pword2 = tk.Entry(frame1, bg="white", show="*")
Pword2.place(x=108, y=232)


# Register button
register1 = tk.Button(
    frame1,
    text="Register",
    fg="black",
    bg="seashell3",
    font=("arial", 12, "bold"),
    width=17,
    height=1
)
register1.place(x=110, y=310)


window.mainloop()
