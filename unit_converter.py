import tkinter

def calculate():
    miles = float(user_input.get())
    lbl_kilometers["text"] = miles * 1.609


window = tkinter.Tk()
window.title("Unit Converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

user_input = tkinter.Entry(width=20)
user_input.pack()

label1 = tkinter.Label(text="Miles")
label1.pack()

lbl_kilometers = tkinter.Label(text="")
lbl_kilometers.pack()

label2 = tkinter.Label(text="Kilometers")
label2.pack()

btn_calculate = tkinter.Button(text="Calculate", command=calculate)
btn_calculate.pack()


window.mainloop()

