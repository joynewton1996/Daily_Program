from algorithm import Algo

obj = Algo()


def solutuion(a):
    print(a)
    max_value = obj.max_value(a)
    factorial = factorial_list(max_value)

    count = 0

    for item in a:
        for item2 in factorial:
            if item == item2:
                count += 1
    if count == len(factorial):
        return 1
    else:
        return 0


def factorial_list(n):
    factorial = []
    step = 0
    while step < n and n > 1:
        k = (n - step)
        step += 1
        factorial.append(k)

    return factorial


if __name__ == "__main__":
    a = [4, 1, 3, 2]
    permutation = solutuion(a)
    print(permutation)
