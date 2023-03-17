#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    #new_dict ={key: a_dictionary[key] for key in keys}
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
