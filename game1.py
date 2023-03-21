# Import tkinter
from tkinter import *
from PIL import ImageTk, Image

import random

# Create a dictionary of the word and its image name
word_img = {
    "bad": "bad.png",
    "bad_2": "bad_2.png",
    "busy": "busy.png",
    "correct": "correct.png",
    "don't want": "don't want.png",
    "fine": "fine.png",
    "finish": "finish.png",
    "forget": "forget.png",
    "go": "go.png",
    "good": "good.png",
    "happy": "happy.png",
    "hello": "hello.png",
    "help": "help.png",
    "how": "how.png",
    "like": "like.png",
    "meet": "meet.png",
    "more": "more.png",
    "need": "need.png",
    "nice": "nice.png",
    "no": "no.png",
    "not": "not.png",
    "please": "please.png",
    "sad": "sad.png",
    "same_them": "same_them.png",
    "same_us": "same_us.png",
    "scared": "scared.png",
    "so so": "so so.png",
    "thanks": "thanks.png",
    "very busy": "very.png",
    "want": "want.png",
    "wrong": "wrong.png",
    "yes": "yes.png",
    "you": "you.png",
    "you_2": "you_2.png",
}


# def word_gen(word_img):
#     word_list = list(word_img.keys())
#     random_word = random.choice(word_list)
#     global the_word
#     b_word.config(text=my_text)


def open_game_1():
    top = Toplevel()
    top.title("Game 1")
    top.geometry('400x600+600+100')

    exit = Button(top,text="Return",command=top.destroy,padx=20,pady=10)
    exit.grid(row=0,column=3)

    global the_word
    the_word = Label(top,text="BLA BLA BLA")
    the_word.grid(row=2, column=2)

    global the_img
    the_img = ImageTk.PhotoImage(Image.open("Signs/----.jpg"))
    l_img = Label(top, image=the_img)
    l_img.grid(row=1, column=2)

    def word_gen(word_img):
        word_list = list(word_img.keys())
        random_word = random.choice(word_list)
        global the_word
        the_word.config(text=random_word)
        img_gen(random_word)

    def img_gen(word):
        file_name = "Signs/" + word + ".png"
        new_img = ImageTk.PhotoImage(Image.open(file_name))
        l_img.config(image=new_img)
        l_img.image = new_img

    b_word = Button(top,text="Generate Word",command=lambda: word_gen(word_img))
    b_word.grid(row=3, column = 2)
    Label(top, text='', width=13).grid(row=1, column=0, rowspan=3, columnspan=2)


def open_game_2():
    top = Toplevel()
    top.title("Game 2")