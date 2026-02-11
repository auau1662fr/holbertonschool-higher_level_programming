#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Première ligne

    for i in range(1, n):
        prev_row = triangle[i-1]
        row = [1]  # Commence toujours par 1

        # Calcul des éléments internes
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])

        row.append(1)  # Termine toujours par 1
        triangle.append(row)

    return triangle
