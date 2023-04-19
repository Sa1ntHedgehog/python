def sumDigitals(string):
    sumNumber=0
    for number in string:
        sumNumber+=int(number)
    return sumNumber   

sumNumbers=sumDigitals(str("5555"))    
print(sumNumbers)