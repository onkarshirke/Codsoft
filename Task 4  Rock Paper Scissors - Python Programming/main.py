import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Rock Paper Scissors')
        self.master.geometry('400x500')
        self.master.config(bg='#2ecc71')

        self.user_score = 0
        self.computer_score = 0
        self.total_games = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text='Rock Paper Scissors', font=('Arial', 24, 'bold'), bg='#2ecc71')
        self.title_label.pack(pady=20)

        self.score_label = tk.Label(self.master, text='Player: 0 | Computer: 0', font=('Arial', 14), bg='#2ecc71')
        self.score_label.pack(pady=10)

        self.choice_label = tk.Label(self.master, text='Choose your option:', font=('Arial', 14), bg='#2ecc71')
        self.choice_label.pack(pady=10)

        self.rock_button = tk.Button(self.master, text='Rock', width=10, command=lambda: self.play('Rock'))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(self.master, text='Paper', width=10, command=lambda: self.play('Paper'))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(self.master, text='Scissors', width=10, command=lambda: self.play('Scissors'))
        self.scissors_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text='', font=('Arial', 14), bg='#2ecc71')
        self.result_label.pack(pady=20)

        self.end_button = tk.Button(self.master, text='End Game', command=self.end_game, bg='red', fg='white')
        self.end_button.pack(pady=10)

        self.ending_label = tk.Label(self.master, text='Made By Onkar', font=('Arial', 10), bg='#2ecc71')
        self.ending_label.pack(side='bottom', pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        result = ''

        if user_choice == computer_choice:
            result = f"It's a tie! Both chose {user_choice}."
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            result = f'You win! {user_choice} beats {computer_choice}.'
            self.user_score += 1
        else:
            result = f'You lose! {computer_choice} beats {user_choice}.'
            self.computer_score += 1

        self.total_games += 1
        self.update_score()
        self.result_label.config(text=result)

    def update_score(self):
        self.score_label.config(text=f'Player: {self.user_score} | Computer: {self.computer_score}')

    def end_game(self):
        total_wins = self.user_score + self.computer_score
        if total_wins == 0:
            feedback = "No games played."
        else:
            user_win_percentage = (self.user_score / total_wins) * 100
            computer_win_percentage = (self.computer_score / total_wins) * 100
            feedback = (f'Final Scores:\n'
                        f'You won {self.user_score} times.\n'
                        f'Computer won {self.computer_score} times.\n'
                        f'Win Rate: You {user_win_percentage:.2f}% | Computer {computer_win_percentage:.2f}%')

        self.result_label.config(text=feedback)
        self.rock_button.config(state='disabled')
        self.paper_button.config(state='disabled')
        self.scissors_button.config(state='disabled')
        self.end_button.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
