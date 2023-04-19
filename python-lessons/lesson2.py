#Print list with a values which inludes in array 'a' and 'b'
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(filter(lambda elem:elem in b,a)))
print(list(set(a) & set(b)))
print(list(set(a) ^ set(b)))

            