my_array=[1,2,3,1,2,2,237,2,2,3,5]

for elem in my_array:
    if elem % 2 == 0:
        print(elem)
    elif elem==237:
        exit()