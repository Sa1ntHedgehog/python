a=[1,2,3,4,5,21,32,33]

def all_unique(numbers):
    return len(numbers)==len(set(numbers))

print(all_unique(a))