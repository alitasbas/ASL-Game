from tkinter import *
from game1 import *
from game2 import *
from game3 import *

global root
root = Tk()
root.title("Home")
# root.grid_columnconfigure(0, weight=1)
# root.maxsize(400, 600)
# root.minsize(400, 600)
root.geometry('400x600+600+100')
# root.resizable(0, 0)

# Header frame to hold out the title and author
header_frame = LabelFrame(root, borderwidth=0, pady=20)
header_frame.pack(side=TOP)
header = Label(header_frame, text="Welcome to my ASL game!", font=('Comic Sans MS', 16), padx=0)
header.grid(row=0)
creator = Label(header_frame, text="By Ali Tasbas", font=('Comic Sans MS', 11))
creator.grid(row=1)


# Body to hold the mini-games
body_frame = LabelFrame(root, pady=0, borderwidth=5)
body_frame.pack()
game_1 = Button(body_frame, text="Guess the sign", font=('Comic Sans MS', 16), borderwidth=0, padx=15, pady=9, command=lambda: open_game_1(root))
game_1.grid(row=0, column=0)
game_2 = Button(body_frame, text="Guess the word", font=('Comic Sans MS', 16), borderwidth=0, padx=15, pady=9, command=lambda: open_game_2(root))
game_2.grid(row=0, column=1)
game_3 = Button(body_frame, text="Letter practice", font=('Comic Sans MS', 16), borderwidth=0, padx=15, pady=9, command=lambda: open_game_3(root))
game_3.grid(row=1, column=0)

# x1 = Label(root, text='filler', width=10).grid(row=1, column=0)
# x2 = Label(root, text='filler', width=10).grid(row=1, column=1)
# x3 = Label(root, text='filler', width=10).grid(row=1, column=2)
# x4 = Label(root, text='filler', width=10).grid(row=1, column=3)

root.mainloop()
