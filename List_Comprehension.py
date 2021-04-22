# You are given three integers x,y,z and representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates (i,j,k) given by on a 3D grid where the sum of (i+j+k) is not equal to .
# conditon 0<= i <=x; o<= j <=y; 0<= k <=z

# Input Format
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = []

# Condition
for i in range(x + 1):  # for outer_loop_variable in outer_sequence:
    for j in range(y + 1):  # for inner_loop_variable in inner_sequence:
        for k in range(z + 1):  # for inner_loop_variable in inner_sequence:
            if i + j + k != n:  # Remove all arrays that sum to n =  to leave only the valid permutations.
                result.append([i, j, k])
print(result)

# Antother method of list comprehension

x, y, z, n = (int(input()) for _ in range(4))

print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if sum([i, j, k]) != n])


