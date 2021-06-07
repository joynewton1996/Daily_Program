def solution(string):
    sub = set([ character for character in string])
    return len(sub)

if __name__=="__main__":
    string =  "abcabcbb"
    result = solution(string)
    print(result)