# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import numpy as np
import agent
def get_user_play():
    play = input(f"Please enter S for Scissors, R for Rock, and P for Paper ")
    play = play.upper()
    return play


def define_user_move(user_type,last_moves=[]):

    user_type = user_type.lower()
    if user_type == "manual":
        user_move = get_user_play()
    elif user_type == "interactive":
        user = agent.Agent(0.33, 0.34, 0.33)
        user_pred = user.predict_move(last_moves)
        user_move = agent.play_next(user_pred)

    else:

        weight_R = input(f"Give the probability (between 0 and 1) for Rock")
        weight_P = input(f"Give the probability (between 0 and 1) for Paper")
        weight_S = input(f"Give the probability (between 0 and 1) for Scissors")
        user = agent.Agent(weight_R, weight_P, weight_S)
        user_move = user.play_move()

    return user_move


def get_computer_play(weights):

    index = np.random.choice(np.arange(0, 3), p=weights)
    choice = ['R', 'P', 'S']
    play = choice[index]

    return play
def is_draw(play1,play2):
    return play1 == play2
def is_winning(user_play,computer_play):
    play_pair=(user_play,computer_play)
    user_winning_pairs=[('R','S'),('P','R'),('S','P')]
    if play_pair in user_winning_pairs:
        return "user"
    else:
        return "computer"



def play(user_type="manual",weights=[0.33,0.33,0.34],last_moves=[]):

    user_play = define_user_move(user_type, last_moves)
    computer_play = get_computer_play(weights)

    draw = is_draw(user_play,computer_play)
    if draw:
        outcome = "no one,it's a draw!"
    else:
        outcome = is_winning(user_play,computer_play)
    return [outcome,computer_play]















# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = int(input(f"Please enter the number of games you wish to play"))
    score = 0
    wins, loses = 0, 0
    last_moves = []
    for i in range(n):

        outcome = play("interactive",[0.8, 0.1, 0.1], last_moves=last_moves)
        last_moves.append(outcome[1])
        if outcome[0]=='user':
            score+=1
            wins+=1
        if outcome[0]=='computer':
            score-=1
            loses += 1

    print(f"The score is {score}, with {wins} wins ans {loses} loses")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
