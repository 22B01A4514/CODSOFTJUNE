#importing tkinter module
from tkinter import *
root = Tk()

#My title
root.title("Haritha's Caluculator")

#Background colour
root.configure(bg='white')

#size of the window
root.geometry("800x600")

#Linking with buttons
def btn_click(item):
    global expression
    expression = expression + str(item)
    text.set(expression)

#clearing
def bt_clear(): 
    global expression 
    expression = "" 
    text.set(expression)

#checking
def bt_equal():
    global expression
    result = str(eval(expression)) 
    text.set(result)
    expression = ""
 
#Setting images
b = PhotoImage(file="C:\\Users\\harit\\OneDrive\\Pictures\\Camera Roll - Copy\\tom1.png")
p = b.subsample(2,2)
label1 = Label(root,image=p)
label1.place(x=90,y=30)


a = PhotoImage(file="C:\\Users\\harit\\OneDrive\\Pictures\\Camera Roll - Copy\\princess.png")
k = a.subsample(3,3)
label1 = Label(root,image=k)
label1.place(x=800,y=0)

c = PhotoImage(file="C:\\Users\\harit\\OneDrive\\Pictures\\Camera Roll - Copy\\doreomon's image.png")
label1 = Label(root,image=c)
label1.place(x=130,y=420)

f = PhotoImage(file = "C:\\Users\\harit\\Downloads\\doremon 2.png")
label2 = Label(root,image=f)
label2.place(x=300,y= 400)


#Building main frame
expression = "" 
text = StringVar()
frame = Frame(root, width=312, height=50, bd=8, highlightbackground="grey", highlightcolor="black", highlightthickness=2)
frame.pack(side=TOP)
input_field = Entry(frame, font=('arial', 18, 'bold'), textvariable=text, width=23, bg="yellow", bd=5, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack() 
btns_frame = Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()


#Buttons
button1 = Button(btns_frame, text = "C", fg = "black", width = 32, height = 4, bd = 2, bg = "teal", cursor = "hand2",command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1) 
button2 = Button(btns_frame, text = "/", fg = "black", width = 10, height = 4, bd = 2, bg = "pink", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
button3 = Button(btns_frame, text = "7", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
button4 = Button(btns_frame, text = "8", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
button5 = Button(btns_frame, text = "9", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
button6 = Button(btns_frame, text = "*", fg = "black", width = 10, height = 4, bd = 2, bg = "pink", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1) 
button7 = Button(btns_frame, text = "4", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
button8 = Button(btns_frame, text = "5", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
button9 = Button(btns_frame, text = "6", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1) 
button10 = Button(btns_frame, text = "-", fg = "black", width = 10, height = 4, bd = 2, bg = "pink", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
button11 = Button(btns_frame, text = "1", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1) 
button12 = Button(btns_frame, text = "2", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
button13 = Button(btns_frame, text = "3", fg = "black", width = 10, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
button14 = Button(btns_frame, text = "+", fg = "black", width = 10, height = 4, bd = 2, bg = "pink", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
button15 = Button(btns_frame, text = "0", fg = "black", width = 21, height = 4, bd = 2, bg = "white", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1) 
button16 = Button(btns_frame, text = ".", fg = "black", width = 10, height = 4, bd = 2, bg = "pink", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
button17 = Button(btns_frame, text = "=", fg = "black", width = 10, height = 4, bd = 2, bg = "sky blue", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
#Ending
root.mainloop()