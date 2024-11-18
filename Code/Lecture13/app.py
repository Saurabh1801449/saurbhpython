import tkinter as tk
import random
from tkinter import messagebox


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
root.configure(bg="#1e1e2f")

board = [" " for _ in range(9)]
player_turn = "X"
computer_mode = False


def minimax(board, depth, is_maximizing):
    winner = check_winner()
    if winner == "X":
        return -10 + depth  
    elif winner == "O":
        return 10 - depth  
    elif winner == "Draw":
        return 0  

    if is_maximizing:  
        best = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  
                best = max(best, minimax(board, depth + 1, False))  
                board[i] = " "  
        return best
    else:  
        best = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  
                best = min(best, minimax(board, depth + 1, True))  
                board[i] = " "  
        return best


def computer_move():
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  
            move_val = minimax(board, 0, False)  
            board[i] = " "  
            if move_val > best_val:
                best_move = i
                best_val = move_val
    board[best_move] = "O"  
    buttons[best_move].config(text="O", fg="magenta")
    winner = check_winner()
    if winner:
        end_game(winner)
    else:
        global player_turn
        player_turn = "X"


def check_winner():
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for (x, y, z) in win_combinations:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return board[x]
    if " " not in board:
        return "Draw"
    return None


def reset_game():
    global board, player_turn
    board = [" " for _ in range(9)]
    player_turn = "X"
    for button in buttons:
        button.config(text=" ", state="normal", bg="#3c3c54", fg="white")


def player_move(index):
    global player_turn
    if board[index] == " ":
        board[index] = player_turn
        buttons[index].config(text=player_turn, fg="cyan" if player_turn == "X" else "magenta")
        winner = check_winner()
        if winner:
            end_game(winner)
        else:
            player_turn = "O" if player_turn == "X" else "X"
            if computer_mode and player_turn == "O":
                root.after(500, computer_move)


def end_game(winner):
    if winner == "Draw":
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
    else:
        messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
    reset_game()


def start_pvp():
    global computer_mode
    computer_mode = False
    reset_game()


def start_pvc():
    global computer_mode
    computer_mode = True
    reset_game()


header = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"), bg="#1e1e2f", fg="white")
header.pack(pady=10)


frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

buttons = []
for i in range(9):
    button = tk.Button(frame, text=" ", font="Arial 20 bold", width=4, height=2,
                       bg="#3c3c54", fg="white", command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)


mode_frame = tk.Frame(root, bg="#1e1e2f")
mode_frame.pack(pady=20)

tk.Button(mode_frame, text="Player vs Player", font="Arial 12 bold", bg="#8e44ad", fg="white",
          command=start_pvp, width=15).grid(row=0, column=0, padx=5, pady=5)

tk.Button(mode_frame, text="Player vs Computer", font="Arial 12 bold", bg="#2980b9", fg="white",
          command=start_pvc, width=15).grid(row=0, column=1, padx=5, pady=5)

tk.Button(root, text="New Game", font="Arial 12 bold", bg="#27ae60", fg="white",
          command=reset_game, width=30).pack(pady=10)


root.mainloop()