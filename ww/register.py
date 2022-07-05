rice_amount = 700
beans_amount = 500
spaghetti_amount = 350
egg_amount = 2000
salt_amount = 100
maggi_amount = 1000

rice_quantity = int(input("how many bags of rice you buy: "))
rice_price = rice_quantity * rice_amount

beans_quantity = int(input("how many bags of beans you buy: "))
beans_price = beans_quantity * beans_amount

spaghetti_quantity = int(input("how many bag of spaghetti did you buy: "))
spaghetti_price = spaghetti_quantity * spaghetti_amount

egg_quantity = int(input("how many crate of eggs did you buy: "))
egg_price = egg_quantity * egg_amount

salt_quantity = int(input("how many bag of salt did you buy: "))
salt_price = salt_quantity * salt_amount

maggi_quantity = int(input("how many bag of maggi did you buy: "))
maggi_price = maggi_quantity * maggi_amount

total_price = rice_price + beans_price + spaghetti_price + egg_price + salt_price + maggi_price


print(f"""
Asher & sons group of company
312 Herbert Macaulay way, Sabo, Yaba
07014014018 florence@gmail.com
********************************************
                              
product      quantity        price 
*********************************************
rice        {rice_quantity}\t           {rice_price}
beans       {beans_quantity}\t           {beans_price}
spaghetti   {spaghetti_quantity} \t           {spaghetti_price}
egg         {egg_quantity} \t           {egg_price}
salt        {salt_quantity} \t           {salt_price}
maggi       {maggi_quantity} \t           {maggi_price}
**********************************************
your total cost is \t       {total_price}
**********************************************

Thanks for shopping with us!!!
""")
