from tkinter import *

root=Tk()
root.title('codemy.com')
root.iconbitmap('')
root.geometry("400x300")

def number():
    try:
        float(my_box.get())
        answer.config(text="That is a number...congrats!")
    except ValueError:
        answer.config(text="That is not a number...")

my_label=Label(root,text="Enter A  Number")
my_label.pack(pady=20)

my_box=Entry(root)
my_box.pack(pady=10)

my_button=Button(root,text="Submit",command=number)
my_button.pack(pady=5)

answer=Label(root,text='')
answer.pack(pady=20)
root.mainloop()