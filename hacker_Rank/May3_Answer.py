from algorithm import Algo
obj = Algo()


def solution(n):
    count = 0
    binary_list = []
    long_gap = 0
    if n % 2 != 0 and n % 4 != 0:
        print(obj.binary(n))
        binary_list = obj.binary(n)
        if binary_list[0] == 1:
            for char in binary_list:
                if char == 0:
                    count += 1
                elif long_gap < count:
                    long_gap = count
                    count = 0
        return print(long_gap)


    else:

        return print(long_gap)


n = int(input())
solution(n)

# n = 5
# binary = []
# count = 0
# if n % 2 != 0 and n % 4 != 0:
#     while n > 0:
#         r = (n % 2)
#         binary.append(r)
#         n = n // 2
#     binary.reverse()
#     print("1st", binary)
#     if binary[0] == 1:
#         for j in range(1, len(binary)):
#
#             if binary[j] == 0:
#                 count += 1
#             # print("count:", count)
#             # print(binary[j])
#             else:
#                 # print("hello")
#                 break
#
#         print(count)
# else:
#     print(count)
