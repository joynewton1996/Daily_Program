def solution(strings):
    my_dict = {"(": ")"}
    a = []
    for item in strings:
        if item in my_dict.keys():
            a.append(item)
        elif item in my_dict.values() and item == my_dict[a.pop()]:
            continue
        else:
            return 0
    if not a:
        return 1
    else:
        return 0


if __name__ == "__main__":
    string = "(()(())())"
    result = solution(string)
    print(result)
