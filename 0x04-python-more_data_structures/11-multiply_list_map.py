#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = list(map(x : x * number, range(len(my_list))))
