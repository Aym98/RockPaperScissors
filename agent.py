import numpy as np


def play_next(predicted_move):

    predicted_move = predicted_move.upper()
    next_move = "P"
    if predicted_move == "S":
        next_move = "R"
    elif predicted_move == "R":
        next_move = "P"
    else:
        next_move = "S"
    return next_move


class Agent:

    def __init__(self, weight_R, weight_P, weight_S):
        self.weights = [weight_R, weight_P, weight_S]

    def predict_move(self, last_moves):

        move = ["R", "P", "S"]
        weights = self.weights
        if len(last_moves) > 10:
            for i in range(3):
                weights[i] = last_moves.count(move[i]) / len(last_moves)
        index = np.random.choice(np.arange(0, 3), p=weights)
        return move[index]

    def play_move(self):

        weights = self.weights
        move = ["R", "P", "S"]
        index = np.random.choice(np.arange(0, 3), p=weights)
        play = move[index]
        return play


