from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")

def demoColorChange():
 btn.configure(bg="yellow", fg="black")

btn = Button(window, text = "Click to Change Color", command= demoColorChange)
btn.pack()
btn.place(x=180,y=180)

window.mainloop()