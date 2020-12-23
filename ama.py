'''x=[13,7,6,50,1,10,23,]
if x[0] == max(x):
    print (x[0], "--->" + " -1 ")
    x.pop(0)
max = max(x)
for i in range(len(x)):
    if x[i]==max or x.index(x[i])==-1:
        print (x[i], "--->" + " -1 ")
    else:
        if x[i] < x[i+1]:
            print (x[i], "---->", x[i+1])
        else:
            print (x[i], "---->" ,max )'''

arr=[13,7,6,50,1,10,23,]
for i in range(0, len(arr),1):
    next = -1
    for j in range(i+1, len(arr),1):
        if arr[i]< arr[j]:
            next = arr[j]
            break
    print(str(arr[i]) + "---" + str(next))