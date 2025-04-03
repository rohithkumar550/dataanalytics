my_list=[10,20,30,40,50]
print(len(my_list)) # 5
print(my_list[0]) # 10
print(my_list[-1]) # 50
# append
my_list.append(60)
print(my_list) # [10, 20, 30, 40, 50, 60]
# insert
my_list.insert(2,25)
print(my_list) # [10, 20, 25, 30, 40, 50, 60]
# remove
my_list.remove(25)
print(my_list) # [10, 20, 30, 40, 50, 60]
# pop
my_list.pop(2)
print(my_list) # [10, 20, 40, 50, 60]

my_list.sort()
print(my_list) # [10, 20, 40, 50, 60]

# reverse
my_list.reverse()
print(my_list) # [60, 50, 40, 20, 10]

# index
print(my_list.index(40)) # 2

# clear
my_list.clear()
print(my_list) # []