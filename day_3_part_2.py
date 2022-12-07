import os
import string


path = '/files/day_3.txt'
data_file = open(os.getcwd()+path, "r")
values_dict = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))
calculation_sum = 0
# iterate through all instructions to calculate sum
group_instruction = []
counter = 0
for row in data_file.readlines():
    counter += 1
    group_instruction.append(row)
    if counter == 3:
        counter = 0
        for letter in group_instruction[0]:
            if letter in group_instruction[1] and letter in group_instruction[2]:
                calculation_sum += values_dict[letter]
                break
        group_instruction = []


print(calculation_sum)


