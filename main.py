
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✓"
reps = 0
finalcheckmark = ""
timer = None

from tkinter import *
window = Tk()
window.title("Pomodoro")
import pygame

pygame.mixer.init()

def play1():
    pygame.mixer.music.load("Campfire.mp3")
    pygame.mixer.music.play(loops=0)

def play2():
    pygame.mixer.music.load("Sky.mp3")
    pygame.mixer.music.play(loops=0)

def play3():
    pygame.mixer.music.load("Rainbow.mp3")
    pygame.mixer.music.play(loops=0)

canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked():
    # my_label.config(text="i am clicked")
    #my_label.config(text=my_input.get())
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    print(reps)
    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Long Break", fg=RED)
        play3()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Short Break", fg=PINK)
        play2()
    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)
        play1()

def reset_clicked():

    global reps, finalcheckmark
    reps = 0
    finalcheckmark = ""
    my_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    my_label3.config(text=finalcheckmark)
    window.after_cancel(timer)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, reps, checkmark, finalcheckmark
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
        minute = count // 60
        second = count % 60
        finaltext = str(minute) + ":" + "{:02d}".format(second)
        canvas.itemconfig(timer_text, text=finaltext)
    else:
        start_clicked()
        window.lift()
        if reps % 2 == 0:
            finalcheckmark = finalcheckmark + checkmark
            my_label3.config(text=finalcheckmark)

# ---------------------------- UI SETUP ------------------------------- #
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 120, image=tomato_img)
timer_text = canvas.create_text(100,140, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2,row=2)
my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Arial", 24, "bold"))
my_label.grid(column=2, row=1)
my_label3 = Label(fg=GREEN, bg=YELLOW, font=("Arial", 8, "bold"))
my_label3.grid(column=2, row=4)


my_button = Button(text="Start", command=start_clicked)
my_button.grid(column=1,row=3)

my_button2 = Button(text="Reset", command=reset_clicked)
my_button2.grid(column=3,row=3)

window.config(padx=100, pady=50, bg=YELLOW)

# window.minsize(width=500, height=300)

#
#
#
#
#
# my_input = tkinter.Entry()
# # my_input.pack()
# my_input.grid(column=4,row=3)

window.mainloop()