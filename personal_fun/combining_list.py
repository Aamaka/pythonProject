import statistics

my_list = [2, 5, 6, 7, 8, 9]
another_list = [1, 3, 4, 10, 11]

my_list.extend(another_list)

print(my_list)
my_list.sort()
print(my_list)

print(statistics.median(my_list))
print(my_list)
