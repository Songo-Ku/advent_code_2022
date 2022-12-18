import os
path_file = os.getcwd() + '/files/day_6.txt'

with open(path_file, "r") as myfile:
    data = myfile.readlines()
data = str(data[1])

# I fixed possibility to not solution exist.
start, end = 0, 14
if len(set(data[start:end])) == 14:
    print('this is number of character processed to be start of packet marker dectect ', end)
else:
    for i in range(14, len(data)-14):
        start += 1
        end += 1
        if len(set(data[start:end])) == 14:
            print('this is number of character processed to be start of packet marker dectect ', end)
            break

    if end == len(data)-14 and len(set(data[start:end])) != 14:
        print(' no solution exist')


