import os
import string


path = '/files/day_3.txt'
data_file = open(os.getcwd()+path, "r")
values_dict = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))
calculation_sum = 0
# iterate through all instructions to calculate sum
for row in data_file.readlines():
    extracted_1 = row[0:int(len(row) / 2)]
    extracted_2 = row[int(len(row) / 2): len(row)]
    # find common letter
    for letter in extracted_1:
        if letter in extracted_2:
            calculation_sum += values_dict[letter]
            break
print(calculation_sum)



