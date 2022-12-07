import os


path = '/files/day_1.txt'
data_file = open(os.getcwd()+path, "r")
counted_calories = 0
dict_3_calories = {"1": 0, "2": 0, "3": 0}

for i in data_file.readlines():
    if i == '\n':
        if counted_calories > dict_3_calories["1"]:
            dict_3_calories["3"] = dict_3_calories["2"]
            dict_3_calories["2"] = dict_3_calories["1"]
            dict_3_calories["1"] = counted_calories
        elif counted_calories > dict_3_calories["2"]:
            dict_3_calories["3"] = dict_3_calories["2"]
            dict_3_calories["2"] = counted_calories
        elif counted_calories > dict_3_calories["3"]:
            dict_3_calories["3"] = counted_calories
        counted_calories = 0
    else:
        counted_calories += int(i)

print(dict_3_calories)
print(sum([dict_3_calories["1"], dict_3_calories["2"], dict_3_calories["3"]]))

