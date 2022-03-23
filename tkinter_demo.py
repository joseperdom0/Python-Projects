import tkinter

window = tkinter.Tk()
window.title("Tkinter Demo")
window.minsize(width=500, height=300)

label1 = tkinter.Label(text="I am a label", font=("Arial",24, "italic"))
# this one situates in the middle
#label1.pack()

# situates left
label1.pack()
label1.config(text="This new text")
label1["text"] = "latest text!"

# Button


def button_got_clicked():
    label1["text"] = input.get()


button1 = tkinter.Button(text="Click me!",command=button_got_clicked)
button1.pack()

# entry

input = tkinter.Entry()
input.pack()



window.mainloop()