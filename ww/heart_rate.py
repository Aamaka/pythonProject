age = int(input("enter your age: "))

maximum_heart_rate = 220 - age

target_heart_rate = (50 / 100) * maximum_heart_rate
target_heart_rate2 = (85 / 100) * maximum_heart_rate

print(f"you are {age} years old \nyour maximum heart rate is {maximum_heart_rate} \n"
      f"your target heart rate ranges from {target_heart_rate} - {target_heart_rate2} ")
