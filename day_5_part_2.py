import os
from itertools import islice
from day_5_extenstion import get_start_pack_data, is_integer, mix_instructions_p2

path_starter = os.getcwd() + '/files/day_5_b.txt'
path_actions = os.getcwd() + '/files/day_5.txt'

main_data_list = get_start_pack_data(path_starter)
with open(path_actions, "r") as myfile:
    action_list = myfile.readlines()

dict_operations = {}
# prepare dict to execute on starter pack data
for i in range(0, len(action_list)):
    if is_integer(action_list[i][6:7]):
        # two digit_number
        a, b = 5, 7
        dict_operations[i] = {
            "move": action_list[i][5:7], "from": action_list[i][b+6:b+7], "to": action_list[i][b+11:b+12]
        }
    else:
        # natural one digit number
        a, b = 5, 6
        dict_operations[i] = {
            "move": action_list[i][5:6], "from": action_list[i][a+7:b+7], "to": action_list[i][a+12:b+12]
        }

for i in range(0, len(dict_operations)):
    main_data_list = mix_instructions_p2(dict_operations[i], main_data_list)
# final result will be save in code variable
code_ = ''
for list_ in main_data_list:
    if list_ != []:
        code_ += str(list_[-1])
print(code_)
