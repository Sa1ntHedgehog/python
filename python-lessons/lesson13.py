def getResult(n):
    return n+(n*n)+(n*n*n)

try:
    print(getResult(int(input())))
except:
    print("Try again")
    print(getResult(int(input())))