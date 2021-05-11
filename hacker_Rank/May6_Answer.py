from algorithm import Algo

obj = Algo()



def solution(a):
    b = obj.sort(a,reverse=True)
    step = 0
    while step < len(b) - 2:
        if b[step] != b[step + 1]:
            return b[step]
        step += 2
    return b[step]



if __name__ == '__main__':
    # Call the fumction
    # a = [9, 3, 9, 3, 9, 7, 9]
    a = [3,3,1,3,1]
    print(solution(a))
    # print(sort(a))
