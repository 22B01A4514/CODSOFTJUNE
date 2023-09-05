from tkinter import *;

#root element
root = Tk()

#title
root.title("My To-do list")
root.configure(bg="papayawhip")

#Frame for listbox
label1 = LabelFrame(root,text="Enter your activities")
label1.pack(pady=40)

#ScrollBar
scroll = Scrollbar(label1)
scroll.pack(side=RIGHT,fill=BOTH)

#Creating a ListBox
box = Listbox(label1,bg="pink",fg="black",bd=2,width=50,height=20,activestyle="none")
box.pack(side=LEFT)
box.config(yscrollcommand=scroll.set)
scroll.config(command=YView)

#Inserting Some activities
my_list = ['Wake Up Early','Breakfast','Going to College','Study','Break']
for i in range(5):
    box.insert(END,my_list[i])

#User_input to add item to listbox
label0 = LabelFrame(root,text="Enter activity")
label0.pack(pady=50)
input = Entry(label0,width=50)
input.pack()

#add function
def add_item():
    box.insert(END,input.get())
    input.delete(0,END)

#delete function    
def delete_item():
    box.delete(ANCHOR)

#Creating add button
label2 = Frame(root)
label2.place(x=480,y=400)
add_button = Button(label2,text="Add item",bg="black",fg="White",bd=2,width=10,height=2,command=add_item)
add_button.pack(side=LEFT,fill=BOTH)

#Creating Delete Button
label3 = Frame(root)
label3.place(x=600,y=400)
rem_button = Button(label3,text="Delete item",bg="black",fg="white",bd=2,height=2,width=10,command=delete_item)
rem_button.pack()

root.mainloop()