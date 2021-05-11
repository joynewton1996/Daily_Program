from algorithm import Algo

obj = Algo()


def solution(a):
    if a >= [0]:
        Max_value = obj.max_value(a)
        sequence = {item for item in range(1, Max_value + 2)}
        a = set(a)
        print(a)
        difference = sequence.difference(a)
        difference = list(difference)
        return difference[0]

    else:
        return 1


if __name__ == '__main__':
    a = [6, 3, 1, 4, 1, 2]
    b = [-1, -3]
    c = [1, 3, 6, 4, 5]
    d = [1, 2, 3, 4]
    seq = solution(a)
    print(seq)
