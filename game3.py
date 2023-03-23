from tkinter import *
from PIL import ImageTk, Image

import random

# Create a dictionary of the letter and image path
letters = {'a': 'Letters/a.png',
           'b': 'Letters/b.png',
           'c': 'Letters/c.png',
           'd': 'Letters/d.png',
           'e': 'Letters/e.png',
           'f': 'Letters/f.png',
           'g': 'Letters/g.png',
           'h': 'Letters/h.png',
           'i': 'Letters/i.png',
           'j': 'Letters/j.png',
           'k': 'Letters/k.png',
           'l': 'Letters/l.png',
           'm': 'Letters/m.png',
           'n': 'Letters/n.png',
           'o': 'Letters/o.png',
           'p': 'Letters/p.png',
           'q': 'Letters/q.png',
           'r': 'Letters/r.png',
           's': 'Letters/s.png',
           't': 'Letters/t.png',
           'u': 'Letters/u.png',
           'v': 'Letters/v.png',
           'w': 'Letters/w.png',
           'x': 'Letters/x.png',
           'y': 'Letters/y.png',
           'z': 'Letters/z.png'}

# TBH I don't know which is lighter to process(Generated by Open AI) :)))))))))
# alphabet_dict = {}
#
# for letter in 'abcdefghijklmnopqrstuvwxyz':
#     alphabet_dict[letter] = f"Letters/{letter.upper()}.png"

five_words = ['Above',
              'Acute',
              'Alive',
              'Alone',
              'Angry',
              'Aware',
              'Awful',
              'Basic',
              'Black',
              'Blind',
              'Brave',
              'Brief',
              'Broad',
              'Brown',
              'Cheap',
              'Chief',
              'Civil',
              'Clean',
              'Clear',
              'Close',
              'Crazy',
              'Daily',
              'Dirty',
              'Early',
              'Empty',
              'Equal',
              'Exact',
              'Extra',
              'Faint',
              'False',
              'Fifth',
              'Final',
              'First',
              'Fresh',
              'Front',
              'Funny',
              'Giant',
              'Grand',
              'Great',
              'Green',
              'Gross',
              'Happy',
              'Harsh',
              'Heavy',
              'Human',
              'Ideal',
              'Inner',
              'Joint',
              'Large',
              'Legal',
              'Level',
              'Light',
              'Local',
              'Loose',
              'Lucky',
              'Magic',
              'Major',
              'Minor',
              'Moral',
              'Naked',
              'Nasty',
              'Naval',
              'Other',
              'Outer',
              'Plain',
              'Prime',
              'Prior',
              'Proud',
              'Quick',
              'Quiet',
              'Rapid',
              'Ready',
              'Right',
              'Roman',
              'Rough',
              'Round',
              'Royal',
              'Rural',
              'Sharp',
              'Sheer',
              'Short',
              'Silly',
              'Sixth',
              'Small',
              'Smart',
              'Solid',
              'Sorry',
              'Spare',
              'Steep',
              'Still',
              'Super',
              'Sweet',
              'Thick',
              'Third',
              'Tight',
              'Total',
              'Tough',
              'Upper',
              'Upset',
              'Urban',
              'Usual',
              'Vague',
              'Valid',
              'Vital',
              'White',
              'Whole',
              'Wrong',
              'Young']

# Might need some more word lists

i = 0

""""
I need help with the photo displaying. I pass the 4 letters.
Everything is set up right, but only after the loop is complete does the image show.
Only the last letter.
"""


def open_game_3(root):

    # Generates a random word from the list and resets the picture
    def word_gen(word_list):
        global random_word
        random_word = random.choice(word_list)
        l_img.config(image=base_img)
        l_img.image = base_img

    # Takes in a word. Keeps the index value right. Shows the picture of the letter based on that index.
    def change_image(the_word):
        global i
        if i < len(the_word):
            the_letter = the_word[i].lower()
            print(the_letter)
            img = ImageTk.PhotoImage(Image.open(letters[the_letter]))
            l_img.config(image=img)
            l_img.image = img
            i = i + 1
        else:
            done_img = ImageTk.PhotoImage(Image.open("Signs/done.png"))
            l_img.config(image=done_img)
            l_img.image = done_img
            i = 0

    top = Toplevel()
    top.title("Game 3")
    top.geometry('400x600+600+100')

    rtrn = Button(top, text="Return", command=top.destroy, padx=20, pady=10)
    rtrn.grid(row=0, column=0)
    Label(top, text='', width=4).grid(row=0, column=3)
    exit = Button(top, text="Exit", command=root.destroy, padx=25, pady=10)
    exit.grid(row=0, column=4)

    global base_img
    base_img = ImageTk.PhotoImage(Image.open("Signs/base.png"))
    l_img = Label(top, image=base_img)
    l_img.grid(row=2, column=2)
    Label(top, text='', height=3).grid(row=1, column=2)

    b_letter = Button(top, text="Next Letter", command=lambda: change_image(random_word))
    b_letter.grid(row=5, column=2)
    b_word = Button(top, text="New Word", command=lambda: word_gen(five_words))
    b_word.grid(row=6, column=2)