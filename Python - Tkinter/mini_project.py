#log in GUI in tkinter python
#must be functionable and interactive
#must be light modern layout
#500x300 size
#-----------------
#build database that can store information(advance!)
#must have another window
#then once inside, it will print the info that you put from the register and to confirm your information
#after that the button will print, "you are now registered.."


import tkinter as tk

window = tk.Tk()


window.title("Log in")
window.geometry("1000x600")
window.resizable(False, False)
window.configure(bg="black")

#not medjo working
frame1 = tk.Frame(window, width=400, height=400, bg="white")
frame1.place(x=300, y=80)


#entries--
#name
#age
#country - string
#gender - checkbutton
#username
#password


name1 = tk.Label(frame1, text="Fullname:", fg="black", bg="white", font=("arial", 12, "italic")).place(x=20, y=20)
name2 = tk.Entry(frame1, bg="white").place(x=100, y=24)


age1 = tk.Label(frame1, text="Age:", fg="black", bg="white", font=("arial", 12, "italic")).place(x=58, y=50)
age2 = tk.Entry(frame1, bg="white").place(x=100, y=55)


place1 = tk.Label(frame1, text="Address:", fg="black", bg="white", font=("arial", 12, "italic")).place(x=25, y=80)
place2 = tk.Entry(frame1, bg="white", width=20).place(x=100, y=85)

#kulang - isa lang dpat pede piliin...
male1 = tk.Checkbutton(frame1, text="Male", bg="lightblue").place(x=20, y=120)
fmale1 = tk.Checkbutton(frame1, text="Female", bg="lightpink").place(x=80, y=120)


line = tk.Label(frame1, text="-------------------------------------------------------", fg="black", bg="white").place(x=20, y=160)

Uname1 = tk.Label(frame1, text="Username:", fg="black", bg="white", font=('arial', 12, "italic")).place(x=20, y=190)
Uname2 = tk.Entry(frame1, bg='white').place(x=108, y=195)

Pword1 = tk.Label(frame1, text="Password:", fg="black", bg="white", font=("arial", 12, "italic")).place(x=20, y=230)
Pword2 = tk.Entry(frame1, bg="white").place(x=108, y=232)











register1 = tk.Button(frame1, text="Register", fg="black", bg="seashell3", font=("arial", 12, "bold"), width= 17, height=1).place(x=110, y=310)



file1 = open("main_file.txt")








window.mainloop()