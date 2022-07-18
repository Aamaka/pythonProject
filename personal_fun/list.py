x = [1, 5, "fghh", 66, 'jnf']

print(x)

x.append(99)

print(x)

x.extend(["aye", 5])

print(x)

x.insert(4, "demola")

print(x)

region = [["ogun", "osun", "lagos"], ["Imo", "Anambra", "Edo"], ["Kano", "kaduna", "kastina"]]
# for a in region:
#     for b in a:
#         print(b)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for c in num:
#     if c % 2 == 0:
#         print(c)

ans = [c for c in num if c % 2 == 0]
con = region + num
print(con)


def palindrome(numb):
    return numb == numb[::-1]


print(palindrome("99999909"))
