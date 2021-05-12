from algorithm import Algo

obj = Algo()


def solution(a):
    if a >= [0]:
        max_value = obj.max_value(a)
        sequence = set(range(1, max_value + 2))
        difference = sequence.difference(a)
        return obj.min_value(difference)

    else:
        return 1


if __name__ == '__main__':
    a = [6, 3, 1, 4, 1, 2]
    b = [-1, -3]
    c = [1, 3, 6, 4, 5]
    d = [1, 2, 3, 4]
    seq = solution(a)
    print(seq)
