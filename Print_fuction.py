# Print the number without using strings

def number(n):
    b = 0
    product = 0
    if 1 <= n <= 150:
        for i in range(1, n + 1):
            temp = (10 ** (n - i)) * i
            a = temp
            product = a + b
            b = product
        print(product)


# Another Method to print the numbers

def num(n):
    for j in range(1, n + 1):
        num = j
        print(num, end='')


number(int(input()))
num(int(input()))