def solution(A):
    non_repeat = []
    for num in a:
        if num not in non_repeat:
            non_repeat.append(num)
    return len(non_repeat)



if __name__=='__main__':
    a = [2,1,1,2,3,1]
    result = solution(a)
    print(result)
