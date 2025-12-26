#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        lis = []
        for j in i:
            lis.append(j * j)
        new_matrix.append(lis)
    return new_matrix
