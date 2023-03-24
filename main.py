from tkinter import *
from game1 import *
from game2 import *
from game3 import *

global root
root = Tk()
root.config(bg='#5a6bdb')
root.title("Home")
# root.grid_columnconfigure(0, weight=1)
# root.maxsize(400, 600)
# root.minsize(400, 600)
root.geometry('400x600+600+100')
# root.resizable(0, 0)

# Header frame to hold out the title and author
header_frame = LabelFrame(root, borderwidth=0, pady=20, bg='#5a6bdb')
header_frame.pack(side=TOP)
header = Label(header_frame, text="Welcome to my ASL game!", font=('Comic Sans MS', 16), padx=0, bg='#5a6bdb')
header.grid(row=0)
creator = Label(header_frame, text="By Ali Tasbas", font=('Comic Sans MS', 11), bg='#5a6bdb')
creator.grid(row=1)


# A blank frame to push the body further down
filler = LabelFrame(root, pady=18, borderwidth=0, bg="#5a6bdb")
filler.pack(fill=X)
Label(filler, text="", bg="#5a6bdb").pack()

# Body to hold the mini-games
body_frame1 = LabelFrame(root, pady=0, borderwidth=0, bg="#bdf52f")
body_frame1.pack()
game_1 = Button(body_frame1, text="Guess the sign", font=('Comic Sans MS', 16), borderwidth=3, padx=15, pady=9, command=lambda: open_game_1(root), bg="#bdf52f")
game_1.grid(row=0, column=0)
game_2 = Button(body_frame1, text="Guess the word", font=('Comic Sans MS', 16), borderwidth=3, padx=15, pady=9, command=lambda: open_game_2(root), bg="#bdf52f")
game_2.grid(row=0, column=1)
body_frame2 = LabelFrame(root, pady=0, borderwidth=0, bg="#bdf52f")
body_frame2.pack()
game_3 = Button(body_frame2, text="Letter practice", font=('Comic Sans MS', 16), borderwidth=3, padx=15, pady=9, command=lambda: open_game_3(root), bg="#bdf52f")
game_3.grid(row=1, column=0)

# x1 = Label(root, text='filler', width=10).grid(row=1, column=0)
# x2 = Label(root, text='filler', width=10).grid(row=1, column=1)
# x3 = Label(root, text='filler', width=10).grid(row=1, column=2)
# x4 = Label(root, text='filler', width=10).grid(row=1, column=3)

root.mainloop()
