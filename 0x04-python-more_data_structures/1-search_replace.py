#!/usr/bin/python3

def search_replace(my_list, search, replace):
    result = []

    for i in my_list:
        if i != search:
            result.append(i)
        elif i == search:
            result.append(replace)
    return result
