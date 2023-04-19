
def fillArray():
    try:
        numbers=[int(number) for number in input().split(',')]
        return numbers
    except ValueError:
        print("Enter correct type of value")
        fillArray()

numbers=[]
numbers=fillArray()
print(numbers)
print(tuple(numbers))