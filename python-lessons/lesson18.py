def countSymbol(findSymbol):
    string="abcdabcd"
    return string.count(findSymbol)

try:
    print(countSymbol((input("Enter symbol which would to find: "))))
except:
    print("Try again")
    print(countSymbol(input()))