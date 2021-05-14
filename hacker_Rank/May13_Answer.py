from algorithm import Algo

obj = Algo()


def solution(s, p, q):
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    master = []
    for i in range(len(p)):
        string = list(s[p[i]:q[i] + 1])
        value = [impact_factor.get(key) for key in string]
        value = obj.min_value(value)
        master.append(value)
    return master


if __name__ == '__main__':
    s = "CAGCCTA"
    p = [2, 5, 0]
    q = [4, 5, 6]
    result = solution(s, p, q)
    print(result)
