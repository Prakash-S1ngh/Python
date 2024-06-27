list = [10,2,3,4,2,4,2,4,3]
list2 = []
for ele in list:
    if list.count(ele)>1 and ele not in list2:
        list2.append(ele)

print(list2)

num_str = "123"
try:
    num_int = int(num_str)
    print(num_int)
except ValueError:
    print("Cannot convert the string to an integer.")
