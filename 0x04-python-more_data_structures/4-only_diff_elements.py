#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    [new_list.append(i)for i in set_1 if i not in set_2]
    [new_list.append(i)for i in set_2 if i not in set_1]

    return (new_list)
