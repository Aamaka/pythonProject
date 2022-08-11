numberOfSteps = 4
a = [2, 4, 5, 67, 8, 9]


# for i in range(numberOfSteps):
#     j = a.pop()
#     a.insert(0, j)
#     print(a)


def positive_sum(arr):
    empty_list = []
    for i in arr:
        if i > 0:
            empty_list.append(i)

    print(sum(empty_list))


m = [3, 6, -4, 7]
positive_sum(m)
