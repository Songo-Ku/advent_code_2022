import os
import re




# this function is easy to custom other solution with changing rows and columns
# it return_ list for each column
def get_start_pack_data(path):
    # prepare list of 8 from main task of day part 1
    list_ = [[] for i in range(9)]
    # I used here better clause "with" in python which automatically close file after skip indent clause.
    with open(path, "r") as myfile:
        rows_ = myfile.readlines()
        schema_rows = rows_[:8]
        for i in range(7, -1, -1):
            # reconstruct data to get same length of rows
            # each row I added one space
            schema_rows[i] = schema_rows[i] + ' '
            if len(schema_rows[i]) < 37:
                # each row is lower than 37 I add 4 speace in while to get same lentgh of rows
                while len(schema_rows[i]) < 37:
                    schema_rows[i] = schema_rows[i] + '    '
            # create dict with borders
            dict_borders = {}
            _val_0, _val_1 = 0, 3
            for val in range(9):
                dict_borders[val] = [_val_0, _val_1]
                _val_0, _val_1 = _val_0 + 4, _val_1 + 4
            # additionally I added regex.
            for ele in range(0, 9):
                value_ = schema_rows[i][dict_borders[ele][0]: dict_borders[ele][1] + 1]
                if value_ != '    ':
                    cleaned_ele = re.findall(r'\[(.*)\]', value_)
                    list_[ele].append(''.join(cleaned_ele))
    return list_


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def mix_instructions_p1(dict_, list_):
    # reverse with use copy in 2 lines
    copy_list = list_[int(dict_["from"])-1][-int(dict_["move"]):]
    copy_list.reverse()
    # it was possible to use list_[::-1] then we had reversed list in one line
    list_[int(dict_["to"])-1] = list_[int(dict_["to"])-1] + copy_list
    list_[int(dict_["from"])-1] = list_[int(dict_["from"])-1][:-int(dict_["move"])]
    return list_


def mix_instructions_p2(dict_, list_):
    print('lista dla wybranego from ', list_[int(dict_["from"])-1])
    # print(' co chcemy przeniesc ', list_[int(dict_["from"])-1][-int(dict_["move"]):])
    copy_list = list_[int(dict_["from"])-1][-int(dict_["move"]):][::-1]
    # it was possible to use list_[::-1] then we had reversed list in one line
    print(copy_list)
    print('gdzie chcemy przeniesc ', list_[int(dict_["to"])-1])

    list_[int(dict_["to"])-1] = list_[int(dict_["to"])-1] + copy_list
    # print(' po przeniesieniu do listy docelowej', list_[int(dict_["to"])-1])
    list_[int(dict_["from"])-1] = list_[int(dict_["from"])-1][:-int(dict_["move"])]
    print(' glowna lista po zmianie\n', list_)
    return list_

