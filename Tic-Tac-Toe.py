import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe By Murtaza")
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text='', font=('Arial', 20), width=10, height=5,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.grid(row=i, column=j, sticky='nsew')
                self.buttons.append(button)

        restart_button = tk.Button(self.master, text="Make it Fresh", font=('Arial', 14), command=self.restart_game)
        restart_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

    def click(self, row, col):
        if self.board[row * 3 + col] == ' ' and not self.current_winner:
            self.board[row * 3 + col] = 'X'
            self.buttons[row * 3 + col].config(text='X', state=tk.DISABLED)
            if self.check_winner('X'):
                self.current_winner = 'X'
                messagebox.showinfo("Winner Mubarak ho", "X wins Mubarak ho!")
            elif ' ' not in self.board:
                self.current_winner = 'Draw'
                messagebox.showinfo("Draw", "It's a draw Dobara khelo!")
            else:
                self.computer_move()

    def computer_move(self):
        if not self.current_winner:
            available_moves = [i for i, spot in enumerate(self.board) if spot == ' ']
            if available_moves:
                square = random.choice(available_moves)
                self.board[square] = 'O'
                self.buttons[square].config(text='O', state=tk.DISABLED)
                if self.check_winner('O'):
                    self.current_winner = 'O'
                    messagebox.showinfo("Winner", "O wins koi faida nahi!")
                elif ' ' not in self.board:
                    self.current_winner = 'Draw'
                    messagebox.showinfo("Draw", "It's a draw Dobara Khelo!")

    def check_winner(self, player):
        for i in range(3):
            # Check rows
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] == player:
                return True
            # Check columns
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        return False

    def restart_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        for button in self.buttons:
            button.config(text='', state=tk.NORMAL)


def main():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
