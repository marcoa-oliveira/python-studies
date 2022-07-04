#Shallow Copy and Deep Copy

list1 = [1,2,3]
print(list1) # //[1,2,3]

copied_list = list1.copy()
print(copied_list)# //[1,2,3]

copied_list.append(4)
print(list1) # //[1,2,3]
print(copied_list)# //[1,2,3,4]
#list1 and copied_list are independent [deep copy]

copied_list2 = list1
print(copied_list2) # //[1,2,3]

copied_list2.append(205)
print(copied_list2) # //[1,2,3,205]
print(list1) # //[1,2,3,205]
#list1 and copied_list2 are connected