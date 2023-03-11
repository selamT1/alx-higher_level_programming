#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    num_elem = len(my_list)
    copy_list = my_list[:]
    if (idx < 0 or idx > num_elem):
        return my_list
    copy_list[idx] = element
    return(copy_list)
