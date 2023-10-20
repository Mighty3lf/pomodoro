from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PEACH = "#FFE4D6"
PINK = "#FACBEA"
PURPLE = "#D988B9"
VIOLET = "#B0578D"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    global reps
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    time.config(text="TIMER", fg="green", bg=PEACH, font=(FONT_NAME, 30, "bold"))
    reps = 0
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_count = WORK_MIN * 60
    short_count = SHORT_BREAK_MIN * 60
    long_count = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_count)
        time.config(text="REST",  fg="red")
    elif reps % 2 == 0:
        count_down(short_count)
        time.config(text="Break")
    else:
        count_down(work_count)
        time.config(text="WORK")

   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor (count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            work_sessions = math.floor(reps / 2)
            new_mark = "✔" * work_sessions
            check_mark.config(text=new_mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PEACH)

canvas = Canvas(width=200, height=224, bg=PEACH, highlightthickness=0)
tomato_img = PhotoImage(file=r"C:\Users\Sami\OneDrive\Ambiente de Trabalho\PY\Pomodoro\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

time = Label(text="TIMER", fg="green", bg=PEACH, font=(FONT_NAME, 30, "bold"))
time.grid(column=1, row=0)

check_mark = Label(text="", fg="green", bg=PEACH, font=(FONT_NAME, 30, "normal"))
check_mark.grid(column=1, row=4)

start = Button(text="START",fg="black", bg=PINK, font=(FONT_NAME, 15, "normal"), command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="RESET",fg="black", bg=PINK, font=(FONT_NAME, 15, "normal"), command=reset_timer)
reset.grid(column=2, row=3)





window.mainloop()