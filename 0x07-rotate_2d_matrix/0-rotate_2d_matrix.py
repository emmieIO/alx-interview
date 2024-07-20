"""Rotation of 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotation of a 2D matrix"""
    # Get the dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the transposed matrix with empty lists
    transposed_matrix = []
    for i in range(cols):
        transposed_matrix.append([0] * rows)
    # print(transposed_matrix);

    #fill in the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    for row in transposed_matrix:
        row.reverse()

    return transposed_matrix
