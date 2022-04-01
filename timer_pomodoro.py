from tkinter import *
#TODO remove GLOBAL

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#WORK_MIN = 25
WORK_MIN = 1
#SHORT_BREAK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
laps = 1
timer = None
mark = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    mark=""
    label.config(text="")
    canvas.itemconfig(timer_text, text = "--:--")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start(laps):
    if (laps % 8 == 0):
        mode.config(text="long break")
        count = LONG_BREAK_MIN * 60
    elif (laps % 2 != 0):
        mode.config(text="normal work")
        count = WORK_MIN * 60
    else:
        mode.config(text="short break")
        count = SHORT_BREAK_MIN * 60
    laps += 1
    count_down(count, laps)
    print(laps)
    global mark
    mark = ""
    for _ in range(laps//2):

        mark+="✔"
    label.config(text=mark)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count,laps):
    #print(f"received laps = {laps}")
    count_min = count // 60
    count_sec = count % 60
    time = f"{count_min:02d}:{count_sec:02d}"
    canvas.itemconfig(timer_text, text = time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, laps)
    else:
        start(laps)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file="./images/tomato.png")
canvas = Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()
button_start = Button(text="Start", command= lambda: start(laps))
button_start.pack()
button_reset = Button(text="Reset", command= reset)
button_reset.pack()
label = Label(text="", bg=YELLOW)
label.pack()

mode = Label(text="Timer", bg=YELLOW)
mode.pack()


window.mainloop()
