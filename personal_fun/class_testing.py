# def add(a: int, b: str) -> tuple[int, str]: position argument
#     return a, b
#
# # print(add(3, "3"))
# #
# #
# #
# # def add(a=2, b="you") -> tuple[int, str]: default argument
# #     return a, b
# #
# # print(add(3))
# # print(add())
# #
#
# # def add(a=2, b="you") -> tuple[int, str]: name argument
# #     return a, b
#
# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
#
#
# print(add(*[1, 2, 3, 4, 5]))
# lst = [7, 9, 3, 10, 56]
# print(add(1, 2, 3, 4, 5,))
# print(add(*lst))
#
#
# def true_false(age):
#     # if age >= 18:
#     #     return True
#     # return False
#
#     return age >= 18
#
#
# def dict_pack_unpack(*args, **kwargs):
#     print("kwargs", kwargs)
#     print("args", args)
#
# dict_pack_unpack(4, 5, "goal", name="hope", age=12, sex="female")
# lst = []
# for i in range(1, 10):
#     lst.append(i)
#     print(lst)
# print()
#
# lst2 = [i for i in range(1, 11)]
# gen = (i for i in range(1, 11))
# print(lst2)
# print(list(gen))
# print()
# lst3 = [i**2 for i in range(1, 11)]
# print(lst3)
# print()
# lst4 = [num for num in range(1, 11)]
# print(lst4)
# print()
# lst_even = [num for num in range(1, 11) if num % 2 == 0]
# print(lst_even)
# print()
# even_and_square_lst = [num if num % 2 == 0 else num ** 2 for num in range(1, 11)]
# print(even_and_square_lst)
#
# print()
# length = int(input("enter the length of your number: "))
# lst_input = [int(input("enter a number: ")) for num in range(length)]
# print(lst_input)
#
# print()
# upper_names = [name.upper() for name in ["dolapo", "tolani", "florence"]]
# print(upper_names)
#
# print()
# list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
# print(list_nested_for)
#
# print()
# # list_of_dicts = [{key: value} for key, value in zip(upper_names, lst_even)]
# # print(list_of_dicts)
#
# print()
# dict_comp = {k: v for k, v in zip(range(5), range(5))}
# print(dict_comp)
#
# s1 = {1, 2, 3, 4, 5, 6}
# print(s1)
#
# s2 = {4, 5, 6, 7, 8, 9}
# print(s2)
#
# s1.add(7)
# print(s1)
#
# # intersection
# print(s1 & s2)

# s1.intersection_update(s1, s2)

# intersection_update
# s1 &= s2
# print(s1)
# print(s2)

# s1.pop()
# print(s1)
#
# # union
# print(s1 | s2)
#
# s1 ^= s2
# print(s1)
# print(s1.symmetric_difference_update(s2))
#
# # super_set
# print(s1 >= s2)
# print(s1)
# print(s2)
#
# # sub_set
# print(s1 <= s2)
#
# dict_play = {"name": "peace", "age": 32, "influenced": "samson"}
# print(dict_play.get("named", "samson"))
#
# print(dict_play.pop("age"))
# print(dict_play)
#
# print(dict_play.popitem())
# print(dict_play)
#
# print(dict_play.update({"surname": "ale", "sex": "male"}))
# print(dict_play)

# def get_first(s: str) -> str:
# #     return s[0][2]
# #
# # l= [get_first(val)for val in ["hello", "how", "Are", "You"]]
# # print(l)
# sum = 0
# lst = []
# for i in range(10):
#     if i % 2 != 0:
#         lst.append(i)
#         sum += i
# print(lst)
# print(sum)

# lst1 = [number := int(input("enter a number: ")) for i in range(10) if i % 2 != 0]
# #
# # print(lst1)
# import string
#
# lst = []
# for i in range(65, 91):
#     lst.append(chr(i))
# print(lst)
#
# print(string.ascii_uppercase)
# lst1 = [chr(i) for i in range(65, 96)]
# lst2 = [ord(i) for i in string.ascii_uppercase]
# print(lst1)
# print(lst2)

# lst2 = []
# for i in range(65, 91):
#     lst2.append(ord(""))
#
# add = lambda x, y: x + y
# sub = lambda x, y: x + y

# print(add.__name__)
# print(sub.__name__)

# def add(a, b):
#     return a + b
#
#
# bay = add(1, 3)
# print(bay)
#
#
# def operate(x, y,  function):
#     return function(x, y)


# val_sub = operate(2, 3,  add)
# print(val_sub)
#
#
# def multiple(x, y):
#     return x * y
#
#
# sar = multiple(2, 3, )
# print(sar)
#
# sire = operate(2, 7, multiple)
# print(sire)

# div = operate(5, 100, lambda x, y, z: y / x)
# print(div)
#
# date = operate(22, 100, lambda x, y: x + y)
# print(date)


# def mul(x, fun):
#     return fun(x)
#
#
# day = mul(3, lambda x: x ** 2)
# print(day)
#
# daytime = mul(4, lambda y: y ** 3)
# print(daytime)

#
# def sub(x, y):
#     return x - y
#
#
# cha = sub(54, 6)
# print(abs(cha))
#
# print(all([2, 5, 6, 2]))
# print(all([2, 5, 6, 2, 0]))
#
# print(any([2, 6, 0, 6, 7]))
#
# print(all([True, False, True]))
# print(any([True, False, True]))
#
# names = ["Amaka", "Segun", "comb", "Samson", "foil"]
# # print((name.istitle()for name in names))
# # print(all(name.istitle() for name in names))
#
# peoples = [{"name": "Ade flo", "age": 30, "year_of_exp": 4, "language": ["java"]},
#          {"name": "Ade wale", "age": 25, "year_of_exp": 4, "language": ["python", "java"]},
#          {"name": "joe flo", "age": 19, "year_of_exp": 4, "language": ["java", "javascript"]},
#          {"name": "peace love", "age": 55, "year_of_exp": 15, "language": ["java", "c++"]},
#          {"name": "love flo", "age": 38,year_of_exp": 4, "language": ["python"]}]
#
# print(all([pole["age"] <= 28 and "python" in pole["language"] for pole in peoples]))
# print(any([people["age"] <= 28 and "python" in people["language"] for people in peoples]))
# print([people["name"] for people in peoples if people["age"] <= 28 and "java" in people["language"]])
# print([people["age"] <= 28 for people in peoples])
#
# lst = map(lambda x: x**2, range(1, 10))
# print(lst)
# lsta = list(map(lambda x: x**2, range(1, 10)))
# print(lsta)
#
# map_object = map(lambda x: x**2, range(1, 10, 2))
# lst1 = list(map_object)
# lst2 = list(map_object)
#
# print(lst1)
# print(lst2)
#
# maps_object = map(lambda x: x**2 if x % 2 == 0 else x, range(1, 10))
# lsts = list(maps_object)
# lsts2 = list(maps_object)
#
# print(lsts)
# print(lsts2)
#

# def is_even(x):
#     return x % 2 == 0
#
#
# filter_obj = list(filter(is_even, range(1, 10)))
# # print(filter_obj)
#
# from functools import reduce
# fruits = ["Apple", "Orange", "Watermelon", "Banana", "Cucumber", "Grapes", "Pear"]
# longest = reduce(lambda x, y: x if len(x) > len(y) else y, fruits)
# print(longest)
#
# smallest = reduce(lambda x, y: x if len(x) < len(y) else y, fruits)
# print(smallest)
# print(max(fruits))
# print(max(fruits, key=len))
# print(sorted(fruits, key=len))
# print(sorted(fruits, key=lambda x: x[-1]))
# print(sorted(fruits, key=len, reverse=True))
#
# fay = "amaka is alive".upper()
# print(fay)
#
# fay = "amaka is alive".split()
# print(fay)
#
# fay = "amaka is alive".count("a")
# print(fay)
#
# fay = "amaka is alive".isprintable()
# print(fay)
#
# fay = "amaka is alive".isspace()
# print(fay)
#
# fay = "           amaka is alive                   ".encode().rstrip().lstrip().strip()
# print(fay.upper())
# for letter in fay:
#     print([letter])
#
# joy = fay[:8]
#
# la = "f" + fay[1:]
# print(la)
# print(joy)
# print(fay)
#
# print(len(fay))

# password = input("enter your password: ")
# pass_word = password[0].upper()
# print(pass_word)
# print(password)

# print(password.find("tu"))
# print(password.replace("e", "a"))

play = {22, 3, 56, 78, 6}
print(min(play))
print(max(play))
print(sum(play))
Range = max(play) - min(play)
print(Range)
x = 2
y = 5
print('x =', x)
