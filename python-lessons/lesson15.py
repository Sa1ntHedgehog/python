a=[1,2,3,4,10,12,23,13,14,6]
b=[1,2,5,11,13,14,15]
c=[]
for elem in a:
    if elem not in b:
        if elem not in c:
            c.append(elem)
print(list(c))

print(list(set(a)-set(b)))