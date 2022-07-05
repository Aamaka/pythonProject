capital = int(input("enter your capital: "))
years = int(input("enter the number of years: "))

investment_rate = 7 / 100

amount = capital * (1 + investment_rate)**years

print(f"your total {amount:.2f}")

gain = amount - capital
print(f"you gain is {gain:.2f}")
