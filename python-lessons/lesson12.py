def getFileFormat(file):
    try:
        format=file.split(".")
        if len(format)>1:
            format=format[1:]
            print(format)
        else:
            print(format[1])
    except:
        print("File have not format")

getFileFormat("test.txt")