def maxDivid(a,b):
    while a % b==0:
        a=a/b
    return a

def isUgly(no):
    no = maxDivid(no, 2)
    no = maxDivid(no, 3)
    no = maxDivid(no, 5)
    return 1 if no is 1 else 0

def getNthUglyNo(n):
    i = 1
    count = 1
    if isUgly(i):
        count += 1
    return 1

no = getNthUglyNo(150)
print(no)