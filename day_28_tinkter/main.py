from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
Font_stuff = FONT_NAME, 25
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 26
reps = 0
counter = None

work_reps = [0, 2, 4, 6]
rest_reps = [1, 3, 5]

columns = [1, 2, 3, 4]
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(counter)
    canvas.itemconfig(timer_text, text="25:00")
    label_time.config(text="Time")
    reps = 0
    label_checkmarks.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    working = True
    long_rest = 7
    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    for n in work_reps:
        if reps == n:
            label_time.config(text="Working", fg=GREEN)
            count_down(work_min_sec)
    for n in rest_reps:
        if reps == n:
            label_time.config(text="Rest", fg=RED)
            count_down(short_break_sec)
    if reps == long_rest:
        label_time.config(text="Long Rest", fg=PINK)
        count_down(long_break_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, **kwargs):
    global reps
    global counter
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" #This is dynamic typing
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        counter = window.after(1000, count_down, count - 1)
    if count == 0:
        reps += 1
        print(reps)
        start_timer()
        marks = ""
        work_reps = math.floor(reps/2)
        for _ in range(work_reps):
            marks += "✔"
            label_checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=70, pady=50, bg="#750E21")


##Photo Image(seeing files)##
tomato_img = PhotoImage(file="tomato.png")

label_time = Label(fg="#BED754", text="Time!", font=Font_stuff, bg="#750E21")
label_time.grid(row=0, column=1)

### Canvas widget ###
canvas = Canvas(width=200, height=224, bg="#750E21", highlightthickness=0)
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(104, 112, text="25:00", font=Font_stuff)
canvas.grid(row=1, column=1)

### Dynamic Typing is the act of changing the type of variable by changing the content within said variable
### e.g: a=5(int) to a="hello"(str)



start_button = Button(text="start", bg="#A5DD9B", fg=RED, command=start_timer)
reset_button = Button(text="reset", bg="#A5DD9B", fg=RED, command=reset_timer)

start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

label_checkmarks = Label(bg="#750E21", fg="#A5DD9B")
label_checkmarks.grid(row=3, column=1)

label_time.config(fg="#A5DD9B")


















window.mainloop()
