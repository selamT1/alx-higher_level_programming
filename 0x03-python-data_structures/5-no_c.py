#!/usr/bin/python3
def no_c(my_string):
    edited_string = []
    for letter in my_string:
        if (letter != 'c' and letter != 'C'):
            edited_string.append(letter)
    return (''.join(edited_string))
