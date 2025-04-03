a="HelloGoodMorning"
print(a[0:5]) # Hello
print(a[5:]) # GoodMorning
print(a[:5]) # Hello
print(a.lower()) # hellogoodmorning
print(a.upper()) # HELLOGOODMORNING
print(a[0:5].lower()) # hello
print(a[0:5].upper()) # HELLO
print(len(a)) # 13
print(a.count('o')) # 2
print(a.startswith('H')) # True
print(a.endswith('n')) # False
print(a.replace("Hello","Hi")) # HiGoodMorning
print(a.count("o")) # 4
print(a.split("Good"))