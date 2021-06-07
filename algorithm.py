class Algo:
    def sort(self, a, reverse=False):
        a = list(a)
        for i in range(len(a) - 1):
            for j in range(i, len(a) - 1):
                if a[i] > a[j + 1]:
                    temp = a[i]
                    a[i] = a[j + 1]
                    a[j + 1] = temp
        if reverse:
            a = a[::-1]
        return a

    def max_value(self, x):

        max_value = self.sort(x)
        return max_value[-1]

    def min_value(self, a):
        min_value = self.sort(a)
        return min_value[0]

    def binary(self, decimal):
        bin_number = []
        while decimal > 0:
            r = decimal % 2
            decimal = decimal // 2
            bin_number.append(r)
        bin_number.reverse()
        return bin_number
    def peak_flag(self,a):
        n = len(a)
        return set(sorted([a[p] for p in range(n) if 0 < p < n - 1 if a[p - 1] < a[p] > a[p + 1]]))
