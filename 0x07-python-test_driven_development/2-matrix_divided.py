
#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Matrix with tests
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for a in matrix:
        for b in a:
            if not isinstance(b, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")


    aray_div = []
    for i in matrix:
        row = []
        for n in i:
            row.append((round(n / div, 2)))
        aray_div.append(row)

    return aray_div

