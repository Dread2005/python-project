import pandas
from tkinter import *
import random
import math
title_font = ("courier", 20, "normal")
word_font = ("courier", 60, "normal")
BACKGROUND_COLOR = "#B1DDC6"

###--------------Pandas Data--------------###
try:
    Spanish_word_data = pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    Spanish_word_data = pandas.read_csv("data/Spanish_English_word_data.csv")

word_list = Spanish_word_data.to_dict(orient="records")
first_word = random.choice(word_list)
current_card = {}
###---------------New Word Gen-------------###


def new_word():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_image)
    current_card = random.choice(word_list)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

###------------Flip Card--------------###


def flip_card():
    global current_card
    global card_back_image
    canvas.itemconfig(canvas_image, image=card_back_image,)
    canvas.itemconfig(card_title, text="english", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    word_list.remove(current_card)
    data = pandas.DataFrame(word_list)
    print(len(data))
    data.to_csv("data/words_to_learn", index=False)
    new_word()


### --------------UI----------------###


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash card")
flip_timer = window.after(3000, func=flip_card)
#window.after_cancel()

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, width=75, height=75, command=new_word)
wrong_button.grid(column=2, row=3)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
canvas_image = canvas.create_image(400, 260, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Spanish", font=title_font)
card_word = canvas.create_text(400, 263, text=first_word["Spanish"], font=word_font)
canvas.grid(column=0, row=0, rowspan=3, columnspan=3, sticky="nsew")
new_word()

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, width=75, height=75, command=new_word and is_known)
right_button.grid(column=0, row=3)
print(len(word_list))















mainloop()

