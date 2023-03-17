#!/usr/bin/python3


def common_elements(set_1, set_2):
    new_list = []
    [new_list.append(i)for i in set_1 if i not in set_2]
    [new_list.append(i)for i in set_2 if i not in set_1]

    return (new_list)
