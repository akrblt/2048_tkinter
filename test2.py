from tkinter import *
import tkinter.font
from tkinter import messagebox
import random

# 2 dimensions list with data
game = [[0, 2, 4, 8],
        [2, 32, 4, 128],
        [2, 32, 32, 128],
        [2, 2, 0, 0]]

colors = {
    0: "#ffffff",
    2: "#f7e50c",
    4: "#f5d99e",
    8: "#f7ac78",
    16: "#de876a",
    32: "#b35231",
    64: "#a40f26",
    128: "#c1efa8",
    256: "#348109",
    512: "#38761d",
    1024: "#9fc5f8",
    2048: "#6fa8dc",
    4096: "#b4a7d6",
    8192: "#c27ba0",
}

labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

dx = 10  # horizontal distance between labels
dy = 10  # vertical distance between labels


def display():
    """Updates the game display with new values and colors."""
    for line in range(len(game)):
        for col in range(len(game[line])):
            bg_color = colors[game[line][col]]
            if game[line][col] > 0:
                labels[line][col].config(text=game[line][col], bg=bg_color, borderwidth=1)
            else:
                labels[line][col].config(text="", bg=bg_color, borderwidth=0)


def pack4(a, b, c, d):
    nm = 0

    if c == 0 and d > 0:
        c, d = d, 0
        nm += 1
    if b == 0 and c > 0:
        b, c, d = c, d, 0
        nm += 1
    if a == 0 and b > 0:
        a, b, c, d = b, c, d, 0
        nm += 1

    if a == b and a > 0:
        nm += 1
        a *= 2
        b, c, d = c, d, 0
    if b == c and b > 0:
        nm += 1
        b *= 2
        c, d = d, 0
    if c == d and d > 0:
        nm += 1
        c *= 2
        d = 0

    return [a, b, c, d], nm


def add_random_tile():
    """Adds a random tile (value 2) in an empty position."""
    empty_cells = []
    for row in range(4):
        for col in range(4):
            if game[row][col] == 0:
                empty_cells.append((row, col))

    if empty_cells:
        row, col = random.choice(empty_cells)
        game[row][col] = 2


def move_down():
    tot_mov = 0
    for col in range(4):
        [game[3][col], game[2][col], game[1][col], game[0][col]], nmove = pack4(game[3][col], game[2][col],
                                                                                game[1][col], game[0][col])
        tot_mov += nmove
    return tot_mov


def move_up():
    tot_mov = 0
    for col in range(4):
        [game[0][col], game[1][col], game[2][col], game[3][col]], nmove = pack4(game[0][col], game[1][col],
                                                                                game[2][col], game[3][col])
        tot_mov += nmove
    return tot_mov


def move_left():
    tot_mov = 0
    for line in range(4):
        [game[line][0], game[line][1], game[line][2], game[line][3]], nmove = pack4(game[line][0], game[line][1],
                                                                                    game[line][2], game[line][3])
        tot_mov += nmove
    return tot_mov


def move_right():
    tot_mov = 0
    for line in range(4):
        [game[line][3], game[line][2], game[line][1], game[line][0]], nmove = pack4(game[line][3], game[line][2],
                                                                                    game[line][1], game[line][0])
        tot_mov += nmove
    return tot_mov


def key_pressed(event):
    """Handles key presses for the game."""
    touche = event.keysym
    moved = False

    if touche == "Right" or touche == "d" or touche == "D":
        moved = move_right()
    elif touche == "Left" or touche == "a" or touche == "A":
        moved = move_left()
    elif touche == "Up" or touche == "w" or touche == "W":
        moved = move_up()
    elif touche == "Down" or touche == "s" or touche == "S":
        moved = move_down()
    elif touche == "Q" or touche == "q":
        result = messagebox.askokcancel("Confirmation", "Do you really want to quit?")
        if result:
            quit()

    if moved:
        add_random_tile()  # Add a new tile if any move was made
        display()  # Update the display after the move


# Construction de la fenêtre:
win = Tk()
win.geometry("800x480")
win.title('2048')

# Title
lbl_title = Label(win, text="2048", height=3, font=("Arial", 15))
lbl_title.pack()

frm_main = Frame(win, bd=5, relief="ridge", bg="lightblue")
frm_main.pack()

# Labels creation
for line in range(len(game)):
    frm = Frame(frm_main)
    frm.pack()

    for col in range(len(game[line])):
        labels[line][col] = Label(frm, width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15))
        labels[line][col].pack(side=LEFT, padx=dx, pady=dy)

display()  # Initial display of the game

win.bind('<Key>', key_pressed)  # Bind key events to the key_pressed function
win.mainloop()
