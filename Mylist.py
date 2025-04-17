#creating an empty list
my_list = []

#Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Inserting 15 to index 1
my_list.insert(1, 15)

#Extending my_list with another list
my_list.extend([50, 60, 70])
print(my_list)

my_list.pop()  #removing the last element
my_list.sort()  #sorting

#finding the index of 30 in my_list
print(my_list.index(30))  
print(my_list)


