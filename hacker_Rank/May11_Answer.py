from algorithm import Algo

obj = Algo()


def solutuion(a):
    max_value = obj.max_value(a)
    series = set(range(1, max_value + 1))
    difference = series.difference(a)
    if difference == set():
        return 1
    else:
        return 0


if __name__ == "__main__":
    a = [4, 1, 3, 2]
    b = [1]
    permutation = solutuion(a)
    print(permutation)
