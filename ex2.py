from numpy.linalg import solve

left = [[1, 1, 1, 1],
        [1, 2, 3, 6],
        [1, 3, 4, 5],
        [1, 4, 7, 7]]

right = [10, 22, 26, 37]

print(solve(left, right))