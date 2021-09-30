#!/c/Python39/python
import sys

if len(sys.argv) < 2:
    while True:
        try:
            value = input()
            if value == '\x04':
                break
            print(value)
        except:
            break
else:
    fileName = sys.argv[1]
    try:
        file = open(fileName, "r")
        print(file.read())
        file.close()
    except:
        print("[ERROR] To manipulate the file")
