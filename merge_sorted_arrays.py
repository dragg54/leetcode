class Solution:
    def merge_sorted_arrays(self, lst1, m, lst2, n):
        last = m + n - 1
        while m > 0 and n > 0:
            if lst1[m - 1] > lst2[n - 1]:
                lst1[last] = lst1[m - 1]
                m -= 1
            else:
                lst1[last] = lst2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            lst1[last] = lst2[n]
            n, last = n-1, last-1