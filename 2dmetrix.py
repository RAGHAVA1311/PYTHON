# 2D matrix in Python

# Example: 3x3 matrix input from user
rows = 3
cols = 3
matrix = [[1 ,2, 3,13],
          [4 ,5, 6,67],
          [7 ,8, 9,89],
          [37, 11, 12, 23]]

# count of prime numbers in the matrix
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    print (num)
    return True

prime_count = 0
for row in matrix:
    for num in row:
        if is_prime(num):
            prime_count += 1
print("Number of prime numbers in the matrix:", prime_count)

# Forest Fire Problem: Count number of separate forests (connected groups of 1s) in a 2D grid

def count_forests(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c): 
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if matrix[r][c] != 1 or visited[r][c]:
            return
        visited[r][c] = True
           # Loop through only 4 possible directions (up, down, left, right)
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(r + dr, c + dc)

    forest_count = 0
    # Iterate through every cell in the matrix
    for i in range(rows):
        for j in range(cols):
            # If the cell is a tree (1) and not visited, it's a new forest
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(i, j)  # Mark all connected trees as visited
                forest_count += 1  # Increment the forest count
    return forest_count

#  Example forest matrix (1 = tree, 0 = empty)
forest_matrix = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0]
]

print("Number of separate forests:", count_forests(forest_matrix))

# Forest fire spread: count unharmed trees after fire starts from (0,0) and spreads in 4 directions
def count_unharmed_trees(matrix, fire_starts):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    burned = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs_fire(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if matrix[r][c] != 1 or burned[r][c]:
            return
        burned[r][c] = True
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs_fire(r + dr, c + dc)
        # In this DFS, backtracking is implicit: after visiting a cell and all its neighbors,
        # the function call returns to the previous cell (the caller).
        # This allows the search to "backtrack" and continue exploring other directions
        # from previous cells, ensuring all connected '1's are visited.
        # The visited (burned) state prevents revisiting and infinite loops.

    # Spread fire from all starting points
    for r, c in fire_starts:
        if matrix[r][c] == 1:
            dfs_fire(r, c)

    unharmed = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not burned[i][j]:
                unharmed += 1
    return unharmed

# Example: fire starts at (0,0) and (0,3)
fire_starts = [(0,0), (0,3)]
print("Number of unharmed trees:", count_unharmed_trees(forest_matrix, fire_starts))





# def binary(n,res = ""):
#     if n == 0:
#         print(res)
#         return
#     binary(n =1,res+"0")
#     binary(n = n-1,res+"1")
# n =2
# binary(n)