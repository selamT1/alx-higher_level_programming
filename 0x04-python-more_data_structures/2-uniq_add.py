#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new_list = []
    [new_list.append(i)for i in my_list if i not in new_list]

    for i in new_list:
        total = total + i

    return (total)
