number = int(input("Enter a number: "))

sum_of_a_factor = 0
factor = 1
while factor < number:
    if number % factor == 0:
        print(factor, "is a factor of", number)
        sum_of_a_factor += factor
    factor += 1

print(sum_of_a_factor)

if sum_of_a_factor == number:
    print(number, "is a perfect number")
elif sum_of_a_factor > number:
    print(number, "it's an abundant number")
else:
    print(number, "it's a deficient number ")
