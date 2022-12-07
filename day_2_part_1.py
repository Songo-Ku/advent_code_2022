import os

path = '/files/day_2.txt'
data_file = open(os.getcwd() + path, "r")

# A for Rock, B for Paper, and C for Scissors.
value_dict_op = {"A": 1, "B": 2, "C": 3}
# X for Rock, Y for Paper, and Z for Scissors
value_dict_me = {"X": 1, "Y": 2, "Z": 3}

my_points = 0

for row in data_file:
    opponent_value, my_value = row.split(sep=' ')
    my_value = my_value[:1]
    if value_dict_op[opponent_value] == value_dict_me[my_value]:
        my_points += (3 + value_dict_op[opponent_value])
    elif opponent_value == "A" and my_value == "Y":
        # it means I won
        my_points += (6 + value_dict_me[my_value])
    elif opponent_value == "A" and my_value == "Z":
        # it means I lost
        my_points += (0 + value_dict_me[my_value])
    elif opponent_value == "B" and my_value == "X":
        # it means I lost
        my_points += (0 + value_dict_me[my_value])
    elif opponent_value == "B" and my_value == "Z":
        # it means I won
        my_points += (6 + value_dict_me[my_value])
    elif opponent_value == "C" and my_value == "X":
        # it means I won
        my_points += (6 + value_dict_me[my_value])
    elif opponent_value == "C" and my_value == "Y":
        # it means I lost
        my_points += (0 + value_dict_me[my_value])

print(my_points)