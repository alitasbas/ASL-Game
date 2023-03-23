from tkinter import *
from PIL import ImageTk, Image
# from tkvideo import tkvideo

import random


word_img = {
    "bad": "Signs/bad.png",
    "bad_2": "Signs/bad_2.png",
    "busy": "Signs/busy.png",
    "correct": "Signs/correct.png",
    "don't want": "Signs/don't want.png",
    "fine": "Signs/fine.png",
    "finish": "Signs/finish.png",
    "forget": "Signs/forget.png",
    "go": "Signs/go.png",
    "good": "Signs/good.png",
    "happy": "Signs/happy.png",
    "hello": "Signs/hello.png",
    "help": "Signs/help.png",
    "how": "Signs/how.png",
    "like": "Signs/like.png",
    "meet": "Signs/meet.png",
    "more": "Signs/more.png",
    "need": "Signs/need.png",
    "nice": "Signs/nice.png",
    "no": "Signs/no.png",
    "not": "Signs/not.png",
    "please": "Signs/please.png",
    "sad": "Signs/sad.png",
    "same_them": "Signs/same_them.png",
    "same_us": "Signs/same_us.png",
    "scared": "Signs/scared.png",
    "so so": "Signs/so so.png",
    "thanks": "Signs/thanks.png",
    "very busy": "Signs/very busy.png",
    "want": "Signs/want.png",
    "wrong": "Signs/wrong.png",
    "yes": "Signs/yes.png",
    "you": "Signs/you.png",
    "you_2": "Signs/you_2.png",
}


def open_game_2(root):

    def img_gen(dic):
        path_list = list(dic.values())
        word_list = list(dic.keys())
        random_path = random.choice(path_list)
        index = path_list.index(random_path)
        global the_word
        the_word = word_list[index]
        # our_word = l_the_word['text']
        # file_name = random_path
        new_img = ImageTk.PhotoImage(Image.open(random_path))
        l_img.config(image=new_img)
        l_img.image = new_img
        e_the_word.delete(0, END)
        e_the_word.insert(0, "")
        # b_check.config(text=the_word)

    def check():
        global count
        global the_word
        global result
        answer = e_the_word.get()
        if answer == the_word:
            e_the_word.delete(0, END)
            # e_the_word.insert(0, "Correct")
            count +=1
            result = "Well Done"
            l_result.config(text=result, fg="#1a8a2d")
            l_counter.config(text=count)
        else:
            e_the_word.delete(0, END)
            # e_the_word.insert(0, "Oops 😣")
            count = 0
            result = "Sorry"
            l_result.config(text=result, fg="#8f0b0b")
            l_counter.config(text=count)
        l_img.config(image=base_img)
        l_img.image = base_img

    top = Toplevel()
    top.title("Game 2")
    top.geometry('400x600+600+100')

    rtrn = Button(top, text="Return", command=top.destroy, padx=20, pady=10)
    rtrn.grid(row=0,column=0)
    Label(top, text='', width=2).grid(row=0, column=2)
    exit = Button(top, text="Exit", command=root.destroy, padx=25, pady=10)
    exit.grid(row=0, column=3)

    # l_video = Label(top)
    # l_video.grid(row=1, column=1)
    # player = tkvideo("S_Clips/volkan yapma.mp4", l_video, loop=1, size=(220, 124), hz=24)
    # player.play()
    global base_img
    global result
    result = ""
    base_img = ImageTk.PhotoImage(Image.open("Signs/base.png"))
    l_img = Label(top, image=base_img)
    l_img.grid(row=2, column=1)
    l_result = Label(top, text=result, pady=10, font=('Comic Sans MS', 26), fg = "#8f0b0b")
    l_result.grid(row=1, column=1)

    global e_the_word
    e_the_word = Entry(top)
    e_the_word.insert(0, "Enter the Word")
    e_the_word.grid(row=4, column=1)
    # global the_word
    # the_word = "Check"
    b_check = Button(top, text="Check", command=check)
    b_check.grid(row=4, column=2)

    b_img = Button(top, text="Show Image", command=lambda: img_gen(word_img))
    b_img.grid(row=5, column=1)
    global count
    count = 0
    l_counter = Label(top, text=count)
    l_counter.grid(row=5, column=2)
    # b_img = Button(top, text="Show Img", command=lambda: img_gen())
    # b_img.grid(row=3, column=2)
    # Label(top, text='', width=13).grid(row=1, column=0, rowspan=3, columnspan=2)


