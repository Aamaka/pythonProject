def my_sum(number):
    x = sum([int(i) for i in str(number)])
    if x > 9:
        result = my_sum(x)
    else:
        result = x
    return result


my_sum(132189)
