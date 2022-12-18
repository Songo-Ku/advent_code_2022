import os
from itertools import islice
from day_5_extenstion import get_start_pack_data, is_integer, mix_instructions

path_starter = os.getcwd() + '/files/day_5_b.txt'
path_actions = os.getcwd() + '/files/day_5.txt'

main_data_list = get_start_pack_data(path_starter)
dict_operations = {'move': '1', 'from': '2', 'to': '7'}

# print(' glowna lista cala \n', main_data_list)
# print('lista dla wybranego from ', main_data_list[int(dict_operations["from"])])
#
# print(' co chcemy przeniesc ', main_data_list[int(dict_operations["from"])][0:int(dict_operations["move"])])
# # main_data_list[int(dict_operations["from"])][0:int(dict_operations["move"])]
# # main_data_list[int(dict_operations["from"])][0:int(dict_operations["move"])]
#
# print('gdzie chcemy przeniesc ', main_data_list[int(dict_operations["to"])])
# main_data_list[int(dict_operations["to"])] = main_data_list[int(dict_operations["from"])][0:int(dict_operations["move"])] + main_data_list[int(dict_operations["to"])]
# print(' po przeniesieniu ', main_data_list[int(dict_operations["to"])])
# main_data_list[int(dict_operations["from"])] = main_data_list[int(dict_operations["from"])][int(dict_operations["move"]):]

# print(main_data_list)
# main_data_list[int(dict_operations["from"])]

result_list_ = mix_instructions(dict_operations, main_data_list)
print(result_list_)
