from operator import itemgetter


#Print dictionary sorted by ASC and DESC
cars=[
    {"brand" : "Mustang"},
    {"brand" : "Honda"},
    {"brand" : "Audi"}
]
print("Sorted by ASC: "+str(sorted(cars,key=itemgetter('brand'))))
print("Sorted by DESC: "+str(sorted(cars,key=itemgetter('brand'),reverse=True)))
