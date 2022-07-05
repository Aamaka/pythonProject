# numbers = (input("enter a two digit number: "))
# print(type(numbers))
#
# firstNumber = (numbers / 10) % 10
# secondNumber = numbers % 10
#
# total = int(firstNumber + secondNumber)
# print(total)

# firstNumber = numbers[0]
# secondNumber = numbers[1]
# print(type(firstNumber))

# total = int(firstNumber) + int(secondNumber)
# print(total)
# print(type(firstNumber))
#
# weight = int(input("enter your weight: "))
# height = float(input("enter your height: "))
# print(type(weight))
# print(type(height))
#
# answer = weight // (height * height)
# print(int(answer))
#
# lst = ['a', 'b', 'c']
# print("".join(lst))
#
# lst = list("glamour")
# print(lst)
# print('d' in lst)
# print('d' not in lst)
# print(lst + [1, 5, 7, 3])
# print(lst * 2)
# print(lst[1:7])
# print(lst[::-1])
#
# list_of_list = [1, 2, [3, 4, 5], 6]
# print(list_of_list[2])
# print(list_of_list[1])
# print(list_of_list)
# print(list_of_list[2][0])
# my_dict = {
#     'name': "segun",
#     'age': 12,
#     'sex': 'male',
#     'hobby': ['python', 'java'],
#     'is_a_wife_beater': False
# }
#
# print('age' in my_dict)
# print(len(my_dict))
# print(my_dict)
#
# for key in my_dict.keys():
#     print(key)
#     print(key, '->', my_dict[key])
#
# for value in my_dict.values():
#     print(value)
#
# for key, value in my_dict.items():
#     print(key, '->', value)
#
# # print(my_dict.items())
# def get_digit(number, position):
#     assert 4 == 2, "4 is not equal to 2"
#
#     return number // (10 ** position) % 10
#
#
# print(get_digit(1234586997, 5))
def get_digit(number: int, position: int) -> int:
    """
    Get the digit at a particular position
    >>> get_digit(234, 0)
    4
    >>> get_digit(234, 2)
    2
    >>> get_digit(234789, 4)
    3
    >>> "hello"
    'hello'
    >>>'2' + 3 # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:



    """

    return number // (10 ** position) % 10
