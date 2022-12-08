import os


path = '/files/day_4.txt'
data_file = open(os.getcwd()+path, "r")
counter = 0
num_help = 0
for row in data_file:
    num_help += 1
    first_, second_ = row.split(sep=",")
    # I used map function only to trening this kind solution, in other situation I will use list comprehension
    first_ = list(map(int, first_.split(sep="-")))
    second_ = second_.split(sep="-")
    # for this solution I assume the max number of digit is 99 and there is no missing data or missing formats
    second_[1] = second_[1][:2]
    second_ = list(map(int, second_))
    if first_[0] <= second_[0] and first_[1] >= second_[1]:
        counter += 1
        continue
    elif first_[0] >= second_[0] and first_[1] <= second_[1]:
        counter += 1
        continue

print(counter)



