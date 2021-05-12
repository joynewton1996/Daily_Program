class Algo:
    def sort(self, a , reverse = False):
        for i in range(len(a) - 1):
            for j in range(i, len(a) - 1):
                if a[i] > a[j + 1]:
                    temp = a[i]
                    a[i] = a[j + 1]
                    a[j + 1] = temp
        if reverse:
            a = a[::-1]
        return a

    def max_value(self,x):
        # print(x)
        for i in range(len(x)-1):
            if x[i] > x[i + 1]:
                temp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = temp

        return x[-1]

    def binary(self,decimal):
        bin_number = []
        while decimal > 0:
            r = decimal % 2
            decimal = decimal // 2
            bin_number.append(r)
        bin_number.reverse()
        return bin_number

    def min_value(self,a , maxvalue = False):
        a = list(a)
        for j in range(len(a) - 1):
            for i in range(len(a) - 1):
                if a[i] > a[i + 1]:
                    temp = a[i]
                    a[i] = a[i + 1]
                    a[i + 1] = temp
        if maxvalue :
            return a[-1]
        else:
            return a[0]



