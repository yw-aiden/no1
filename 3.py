def sort_list(x, n):
    i = x.index(n)
    x[0], x[i] = x[i], x[0]
    i = 0
    j = len(x) - 1
    while i < j:
        while i < j and x[j] >= n:
            j = j - 1
        x[i], x[j] = x[j], x[i]
        while i < j and x[i] <= n:
            i = i + 1
        x[i], x[j] = x[j], x[i]
    return x


a = [2, 8, 4, 6, 5, 9, 1, 3, 7]
print(sort_list(a, 4))
