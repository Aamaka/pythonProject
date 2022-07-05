print("welcome to tip calculator")
bill = float(input("what is the total bill?: \n"))
no_of_people = int(input("how many people will spilt the money?: \n"))
percentage = int(input("how many percent would you like to give?  10, 12 or 15: \n"))

total = float(bill * (percentage / 100))
answer = float((total + bill) / no_of_people)
print(answer)
