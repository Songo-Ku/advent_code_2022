import os

path = '/files/day_2.txt'
data_file = open(os.getcwd() + path, "r")

# A for Rock, B for Paper, and C for Scissors.
value_dict_op = {"A": 1, "B": 2, "C": 3}
# X for Rock, Y for Paper, and Z for Scissors
value_dict_me = {"X": 1, "Y": 2, "Z": 3}

my_points = 0

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
for row in data_file:
    opponent_value, expected_result = row.split(sep=' ')
    expected_result = expected_result[:1]
    if expected_result == "Y":
        # it means draw
        my_points += (3 + value_dict_op[opponent_value])
    elif expected_result == "X":
        # it means I need to lose and find lose figure
        if opponent_value == "A":
            my_points += (0 + value_dict_me["Z"])
        elif opponent_value == "B":
            my_points += (0 + value_dict_me["X"])
        elif opponent_value == "C":
            my_points += (0 + value_dict_me["Y"])
    else:
        # it means I need to win
        if opponent_value == "A":
            my_points += (6 + value_dict_me["Y"])
        elif opponent_value == "B":
            my_points += (6 + value_dict_me["Z"])
        elif opponent_value == "C":
            my_points += (6 + value_dict_me["X"])
print(my_points)