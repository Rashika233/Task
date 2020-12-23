from sys import argv
NameOfProgram, NameOfFile = argv

print('The name of my program is :', NameOfProgram)
print('The name of my file is :', NameOfFile)

while True:
    try:
        fh=open(NameOfFile)
        content=fh.read()
        print(content)
        break
    except:
        print('You have gievn the wrong name')
       