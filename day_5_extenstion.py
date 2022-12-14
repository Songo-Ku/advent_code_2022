import os
import re


path = os.getcwd() + '/files/dataset_1.txt'


# this function is easy to custom other solution with changing rows and columns
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




