import tkinter

window = tkinter.Tk()
window.title("Tkinter Demo")
window.minsize(width=500, height=300)

label1 = tkinter.Label(text="I am a label", font=("Arial",24, "italic"))
# this one situates in the middle
#label1.pack()

# situates left
label1.pack(side="left")
window.mainloop()