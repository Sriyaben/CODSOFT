import tkinter as tk
from tkinter import messagebox
import random

# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]
player = "X"
ai = "O"

# Create a GUI window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Function to check if the board is full
def is_board_full(board):
    return " " not in board

# Function to check if a player has won
def check_winner(board, player):
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to make the AI move using Minimax
def ai_move():
    best_score = float("-inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, ai):
        return 1
    elif check_winner(board, player):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = ai
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function to handle player's move
def player_click(button):
    global player

    if board[button] == " ":
        buttons[button].config(text=player)
        board[button] = player

        if check_winner(board, player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player} wins!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            root.quit()
        else:
            player = ai
            ai_button = ai_move()
            buttons[ai_button].config(text=ai)
            board[ai_button] = ai

            if check_winner(board, ai):
                messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
                root.quit()
            elif is_board_full(board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                root.quit()
            else:
                player = "X"

# Create buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=" ", font=("normal", 20), width=5, height=2, command=lambda i=i: player_click(i))
    button.grid(row=row, column=col)
    buttons.append(button)

# Start the GUI main loop
root.mainloop()
