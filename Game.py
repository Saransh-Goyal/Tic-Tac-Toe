from tkinter import *
from tkinter import messagebox

root = Tk()
canvas =Canvas(root)
canvas.pack()
player = 'X'
original = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
updated = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
count = 0
win_string = ""

for i in range(3):
    for j in range(3):
        original[i][j] = Button(canvas, bg='white', width=4, font='Arial 30', command=lambda r=i, c=j:enter_value(r, c))
        original[i][j].grid(row=i, column=j)


def enter_value(r, c):

    global player, count
    if player == 'X' and updated[r][c] == 0:
        original[r][c].config(text='X')
        updated[r][c] = 'X'
        check_winner()
        player = 'O'
    elif player == 'O' and updated[r][c] == 0:
        original[r][c].config(text='0')
        updated[r][c] = 'O'
        check_winner()
        player = 'X'


def check_winner():
    global count, player, win_string
    for i in range(3):
        if updated[i][0] == updated[i][1] == updated[i][2] != 0:         # Rows
            win_string = f'Congratulations! player {player} wins'
        elif updated[0][i] == updated[1][i] == updated[2][i] != 0:       # Columns
            win_string = f'Congratulations! player {player} wins'
        elif updated[0][0] == updated[1][1] == updated[2][2] != 0:       # Diagonal 1
            win_string = f'Congratulations! player {player} wins'
        elif updated[2][0] == updated[1][1] == updated[0][2] !=0:       # Diagonal 2
            win_string = f'Congratulations! player {player} wins'
        elif count == 9:
            win_string = 'TIE', 'Oops! game tie'
    count += 1
    show_status(win_string)


def show_status(state):
    global player, original, updated, count, win_string
    if state != "":
        messagebox.showinfo('Result', state)
        player = 'X'
        original = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        updated = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        count = 0
        win_string = ""
        for i in range(3):
            for j in range(3):
                original[i][j] = Button(canvas, bg='white', width=4, font='Arial 30',
                                        command=lambda r=i, c=j: enter_value(r, c))
                original[i][j].grid(row=i, column=j)

root.title('Tic Tac Toe')
root.resizable(False, False)
root.mainloop()
