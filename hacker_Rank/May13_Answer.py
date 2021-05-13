from algorithm import Algo

obj = Algo()


def solution(s, p, q):
    print(s)
    # A = 1
    # C = 2
    # G = 3
    # T = 4
    # K = 0
    string = []
    a =[]
    m = len(p)

    for i in range(m):
        for j in range(p[i], q[i] + 1):
            string.append(s[j])
        minvalue = obj.min_value(string)
        string = []
        a.append(minvalue)
    return a


if __name__ == '__main__':
    s = "CAGCCTA"
    p = [2, 5, 0]
    q = [4, 5, 6]
    result = solution(s, p, q)
    print(result)
