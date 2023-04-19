#Print value from array that less then 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elem in a:
    if elem<=5:
        print(elem)
    else: 
        print(str(elem)+" greater then 5")
print(list(filter(lambda elem: elem<=5,a)))