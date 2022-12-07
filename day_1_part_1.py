import os


path = '/files/day_1.txt'
data_file = open(os.getcwd()+path, "r")
counter = 0
index_val_list = [0, 0]
index_ = 1

for i in data_file.readlines():
    if i == '\n':
        if counter > index_val_list[1]:
            print('jestem w wiekszym rekordzie')
            index_val_list[0], index_val_list[1] = index_, counter
            print('po zmianie lidera')
            print('indeks: ', index_val_list[0], 'value:  ', index_val_list[0])
            # current_val[0] = counter_renifer
        elif counter == index_val_list[1]:
            print('huston mamy problem 2x taki sam wynik', 'dla pozycji  ', index_val_list[0])
        counter = 0
        index_ += 1
    else:
        counter += int(i)

print(index_val_list)