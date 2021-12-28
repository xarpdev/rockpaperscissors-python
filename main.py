"""
Implementation of rock, paper, scissors by Santiago Fabián Quispe (XarpDEV)
"""

import random

def play():
    print("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = input("Player: ")
    computer = random.choice(['r','p','s'])
    print("You Opponent used: " + computer)

    if user == computer:
        return 'It\'s a tie'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())