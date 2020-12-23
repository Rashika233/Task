m=int(input('Enter the no of rows'))
n=int(input('Enter the no of coloumns'))

a=[]
for i in range(m):
    b=[]
    for j in range(n):
        b.append(j)
    a.append(b)


for i in range(m):
    for j in range(n):
        print(a[i][j])
    print()

row=0
col=0
while row < m and col < n:
    for i in range(col, n):
        print(a[row][i])
    row = row+1
    for i in range(row, m):
        print(a[i][n-1])
    n = n-1
    if row < m:
        for i in range(n-1, (col-1), -1):
            print(a[m-1][i])
        m=m-1
    if col < n:
        for i in range(m-1, row-1, -1):
            print(a[i][col])
        col=col+1