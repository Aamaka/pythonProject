# miles = int(input("enter miles: "))
# gallons = int(input("enter number of gallon(s): "))
# mile = 0
#
# while mile != -1:
#
#     gallons = float(input("enter number of gallon(s) -1 to end: "))
#     if gallons == -1:
#         break
#
#     miles = int(input("enter miles: "))
#     answer = miles / gallons
#     print("the miles per gallons is ", answer)
# print(mile)


count = 0
total_gallon = 0
total_miles = 0
miles_per_gallon = 0
gallons = float(input("Enter the gallons used, -1 to end: "))
miles = int(input("Enter the miles driven: "))

while gallons != -1:
    count += 1
    miles_per_gallon = miles / gallons
    print(f"The miles/gallons for this tank was {miles_per_gallon: .2f}")

    miles = int(input("Enter the miles driven: "))
    gallons = float(input("Enter the gallons used, -1 to end: "))

average = miles_per_gallon / count
print(f"The overall average miles / gallon was {average: .2f}")
