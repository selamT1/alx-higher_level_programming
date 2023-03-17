#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = [[elem * elem for elem in inner]for inner in matrix]
    return copy_matrix
