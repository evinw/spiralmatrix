def print_spiral(n: int):
    # Initialize the matrix with zeroes
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Set the initial position and direction
    x, y = 0, 0
    dx, dy = 0, 1

    # Iterate over the range of numbers
    for i in range(1, n * n + 1):
        # Set the current position to the current number
        matrix[x][y] = i

        # Check if the next position in the current direction is out of bounds
        if (x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n or matrix[x + dx][y + dy] != 0):
            # Change direction
            dx, dy = dy, -dx

        # Move to the next position
        x += dx
        y += dy

    # Print the matrix
    for i in range(n):
        for j in range(n):
            print(f"({i}, {j}): {matrix[i][j]}")
        print()

print_spiral(5)
