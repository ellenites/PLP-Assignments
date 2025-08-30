my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1,15)
otherlist=[50,60,70]
my_list.extend(otherlist)
my_list.pop(-1)
my_list.sort()
print(my_list)
print(30 in my_list)
index = my_list.index(30)
print(index)