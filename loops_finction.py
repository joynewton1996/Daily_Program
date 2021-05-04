def attempts(n):
    x = 1
    while x <= n:
        print("Attempts " + str(x))
        x += 1

    print("Done")


attempts(5)


def sum_divisors(n):
    sum = 0
    x = 1
    while x < n:
        if n % x == 0:
            sum = sum + x
            x += 1


        else:
            x += 1
    # Return the sum of all divisors of n, not including n
    return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51


# 114


def multiplication_table(table_number):
    multiplier = 1
    while multiplier <= 10:
        result = table_number * multiplier
        print(str(table_number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


# multiplication_table(85)

number = [22, 52, 59, 37, 48]
sum = 0
length = 0

for x in number:
    sum += x
    length += 1
print("Total sum: " + str(sum) + " - Average: " + str(sum / length))


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        print(i)
        result = i * result
    return result


print(factorial(5))


def celsius_table(x):
    return (x - 32) * 5 / 9


for x in range(1, 101, 20):
    print(x, celsius_table(x))

# Nested loops

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print("Hello")

ipl_2021 = ["RCB", "KKR", "CSK", "Mi"]
for team_A in ipl_2021:
    for team_B in ipl_2021:
        if team_A != team_B:
            print(team_A + " Vs " + team_B)


def is_valid(user):
    if len(user) > 3:
        return validate_users(user)


def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")


validate_users(["purplecat"])


def sum_positive_number(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum


print(sum_positive_number(5))


def celsius_converter(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print(str(x) + " and " + str(celsius_converter(x)))

ipl = ["RCB", "KKR", "MI", "CSK"]

for x in ipl:
    for y in ipl:
        if x != y:
            print(x + " vs " + y)
        else:
            print("same")


def factorial(i):
    result = 1
    for x in range(1, i+1):
        result = x * result
    return result


for i in range(0, 10):
    print(str(i) + " and factorial is " + str(factorial(i)))



def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)
#print(factorial(99))

def first_and_last(message):
    print(message[0])
    print(message[-1])
    if message[0] == message[-1] or message[0] == "":
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))