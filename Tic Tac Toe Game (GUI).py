import tkinter as tk
from tkinter import messagebox

# Initialize game state
board = ["-"] * 9
currentplayer = "X"
winner = None
gamerunning = True

# Function to check for a win or tie
def checkforwin():
    global winner, gamerunning
    # Horizontal
    for i in [0, 3, 6]:
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            winner = board[i]
            return True
    # Vertical
    for i in [0, 1, 2]:
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            winner = board[i]
            return True
    # Diagonal
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkfortie():
    return "-" not in board and winner is None

def button_click(index):
    global currentplayer, gamerunning

    if board[index] == "-" and gamerunning:
        board[index] = currentplayer
        buttons[index].config(text=currentplayer, state="disabled")
        if checkforwin():
            status_label.config(text=f"Winner: {winner}")
            gamerunning = False
            disable_all_buttons()
            return
        elif checkfortie():
            status_label.config(text="It's a tie!")
            gamerunning = False
            return

        currentplayer = "O" if currentplayer == "X" else "X"
        status_label.config(text=f"{currentplayer}'s turn")

def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def reset_game():
    global board, currentplayer, winner, gamerunning
    board = ["-"] * 9
    currentplayer = "X"
    winner = None
    gamerunning = True
    status_label.config(text=f"{currentplayer}'s turn")
    for btn in buttons:
        btn.config(text="-", state="normal")

# Create GUI window
root = tk.Tk()
root.title("Tic Tac Toe")

# Status label
status_label = tk.Label(root, text="X's turn", font=("Arial", 16))
status_label.grid(row=0, column=0, columnspan=3)

# Buttons for the board
buttons = []
for i in range(9):
    btn = tk.Button(root, text="-", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=(i//3)+1, column=i%3)
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

# Start GUI loop
root.mainloop()
