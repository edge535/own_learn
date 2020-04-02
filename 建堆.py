li = [0, 83, 34, 12, 5, 1, 2, 4, 6, 7, 8, 9, 23, 74, 37, 44]


def sift(li, k, m):
    i = k
    j = 2 * i
    x = li[k]
    while j <= m:
        if (j < m) and (li[j] > li[j + 1]):
            j += 1
        if x < li[j]:
            break
        else:
            li[i] = li[j]
            i = j
            j = 2 * i
    li[i] = x


def headsort(li):
    # for i in [7, 6, 5, 4, 3, 2, 1]:
    #     sift(li, i, 15)
    for i in [6, 5, 4, 3, 2, 1]:
        sift(li, i, len(li))


print(li)
sift(li, 1, len(li))
print(li)

headsort(li)
print(li)


