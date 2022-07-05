year = 1
capital = int(input("enter your capital: "))

investment_rate = 7 / 100

print("""year\t  amount
************************** """)
while year <= 30:
    amount = capital * (1 + investment_rate)**year
    print(f"""{year}\t     {amount:.2f}
*************************************""")
    year += 1
