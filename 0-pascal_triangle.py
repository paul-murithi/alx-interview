def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the Pascal's Triangle

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # The first element of each row is always 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # The last element of each row is always 1
        triangle.append(new_row)

    return triangle

if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
