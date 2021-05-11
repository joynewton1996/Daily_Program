from algorithm import Algo

obj = Algo()


def solutuion(a):
    print(a)
    max_value = obj.max_value(a)
    factorial = factorial_list(max_value)
    for item in factorial:
        if item not in a:
            return 0
        else:
            return 1


def factorial_list(n):
    factorial = []
    step = 0
    while step < n and n > 1:
        k = (n - step)
        step += 1
        factorial.append(k)

    if n == 1:
        return factorial[1]

    return factorial


if __name__ == "__main__":
    a = [4, 1, 3, 2]
    permutation = solutuion(a)
    print(permutation)
