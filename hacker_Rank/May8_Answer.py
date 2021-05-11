from algorithm import Algo

obj = Algo()


def solution(a):
    if a >= [0]:
        Max_value = obj.max_value(a)
        sequence = sequence_generator(Max_value)
        result = []
        for value in sequence:
            if value not in a:
                result.append(value)

        if result > []:
            result = obj.sort(result)
            return result
        else:
            result.append(Max_value + 1)
            return result
    else:
        return [1]


def sequence_generator(n):
    sequence = []
    step = 1
    while step <= n:
        sequence.append(step)
        step += 1
    return sequence


if __name__ == '__main__':
    a = [6, 3, 1, 4, 1, 2]
    seq = solution(a)
    print(seq)
