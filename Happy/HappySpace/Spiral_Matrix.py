
def spiral_order(matrix):
    result = []

    while matrix:
        # Traverse the first row
        result += matrix[0]
        matrix.pop(0)

        if matrix and matrix[0]:
            # Traverse the last column
            for row in matrix:
                result.append(row[-1])
                row.pop()

        if matrix:
            # Traverse the last row in reverse order
            result += matrix[-1][::-1]
            matrix.pop()

        if matrix and matrix[0]:
            # Traverse the first column in reverse order
            for row in matrix[::-1]:
                result.append(row[0])
                row.pop(0)

    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = spiral_order(matrix)
print(result)
print(matrix)