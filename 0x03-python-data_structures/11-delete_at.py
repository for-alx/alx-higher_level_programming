#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    if len(my_list) < 0:
        return my_list
    elif len(my_list) < idx:
        return my_list
    else:
        my_list.remove(idx)
        return my_list
