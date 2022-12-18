import os


path = '/files/day_4.txt'
data_file = open(os.getcwd()+path, "r")
helP_var = 0
counter = 0
for row in data_file:
    # helP_var += 1
    # if helP_var > 10:
    #     break
    P_, D_ = row.split(sep=",")
    # This time I used better solution list comprehension (faster one)
    P_ = [int(x) for x in P_.split(sep="-")]
    D_ = D_.split(sep="-")
    # for this solution I assume the max number of digit is 99 and there is no missing data or missing formats
    D_[1] = D_[1][:2]
    D_ = [int(x) for x in D_]
    print(P_, ' _____ ', D_)
    # [6, 87]    _____[87, 88]
    # [55, 59] _____[54, 58]
    if P_[0] > D_[1] or D_[0] > P_[1]:
        print(' zadzialal mechanizm 4 i nie dodal ')
        # 4 examples 10,20 | 1,2;    10,20 | 50,99;
        # there is no overlap
        continue

    if P_[0] == D_[0] or P_[0] == D_[1] or P_[1] == D_[1] or P_[1] == D_[0]:
        print(' nr ', helP_var)
        # 1 examples 2,2 | 1,2;    3,3 | 3,99;    1,30 | 5,30;    66,69 | 69,99;
        print(' zadzialal mechanizm 1')
        counter += 1
        continue

    if P_[0] > D_[0] and P_[0] < D_[1]:
        print(' zadzialal mechanizm 2')
        # 2 examples 77,99 | 20, 78
        counter += 1
        continue

    # solution 8 include solution 3
    if P_[0] > D_[0] and P_[1] > D_[1]:
        print(' zadzialal mechanizm 3')
        # 3 examples 77,99 | 20, 77
        counter += 1
        continue

    if P_[1] > D_[1] and P_[0] < D_[1]:
        print(' zadzialal mechanizm 5')
        # 5 examples 70,99 | 71,80
        counter += 1
        continue

    if D_[1] > P_[1] and P_[1] > D_[0]:
        print(' zadzialal mechanizm 6')
        # 6 examples 40,60 | 50,99
        counter += 1
        continue

# czy ono ma sens ?
    if P_[0] < D_[0] and P_[1] > D_[0]:
        print(' zadzialal mechanizm 7')
        # 7 examples 5,50 | 10,51
        counter += 1
        continue

# this one is better than example 3
    if P_[0] > D_[0] and D_[1] > P_[0]:
        print(' zadzialal mechanizm 8')
        # 8 examples 30,50 | 10, 88
        counter += 1
        continue

    if P_[0] < D_[1] and P_[0] > D_[0]:
        print(' zadzialal mechanizm 9')
        # 9 examples 30,50 | 10, 88
        counter += 1
        continue













    # if P_[1] == D_[0] or P_[0] >= D_[1] or (P_[1] >= D_[1] and P_[0] >= D_[0]):
    #     # examples
    #     counter += 1
    #     continue
    # if P_[0] >= D_[0] and P_[1] <= D_[1]:
    #     # examples
    #     counter += 1
    #     continue
    # if P_[1] >= D_[0] and P_[0] >= D_[0]:
    #     counter += 1
    #     continue
    # if P_[1] <= D_[1] and P_[0] <= D_[0]:
    #     # <<<<<<<<<<<<<<<<<<<<<<<<<<
    #     # <<<<<<<<<<<<<<<<<<<<<<<<<<<
    #     #  to moze byc zle
    #     continue






    # [55, 59] _____[54, 58]


print(counter)
# it delivery the solution which select only records which doesnt overlap at all
# if P_[1] > D_[0] or P_[0] < D_[1]:
#     counter += 1
#     continue




# with open(os.getcwd() + '/files/day_5_b.txt', 'r') as fin:
#     data = fin.read().splitlines(True)[:-1]
#     print(data)

import re
re.findall('..','1234567890')
# ['12', '34', '56', '78', '90']