import os
path_file = os.getcwd() + '/files/day_6.txt'

with open(path_file, "r") as myfile:
    data = myfile.readlines()
data = str(data[0])

# risk of this solution is that if there is no sulution the program will not inform about it
start, end = 0, 4
if len(set(data[start:end])) == 4:
    print('this is number of character processed to be start of packet marker dectect ', end)
else:
    for i in range(4, len(data)-4):
        start += 1
        end += 1
        if len(set(data[start:end])) == 4:
            print('this is number of character processed to be start of packet marker dectect ', end)
            break






