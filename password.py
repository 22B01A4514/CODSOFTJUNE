from tkinter import *;

#importing string
import string

#importing random
import random

root = Tk()

#background colour
root.configure(bg='aquamarine')
root.geometry('500x300')
root.title("My password generator")

#Frame to enter length of the password we want
label1 = LabelFrame(root,text="Enter Length of the Password",fg="black",width=500,height=600)
label1.pack(pady=10)
user_input = Entry(label1,width=50,font=2,fg="red")
user_input.pack()

#Displaying output through this frame
label3 = LabelFrame(root,width=50)
label3.pack()
password = Entry(label3,text="",width=75)
password.pack()


#Main logic
def random_password():
    password.delete(0,END)
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    special_char = string.punctuation
    digits = string.digits
    total = lower_case + upper_case + special_char + digits
    length = int(user_input.get())
    text = ""
    for i in range(length):
        text += random.choice(total)
    password.insert(0,text)

def reset():
   password.delete(0,END)
   user_input.delete(0,END)


#Creating Button
button = Button(root,text="Generate Password",fg="white",bg="black",command=random_password)
button.place(x=23,y=100)

button2 = Button(root,text="Reset all",bg="Black",fg="White",command=reset)
button2.place(x=200,y=100)

#End of the program
root.mainloop()