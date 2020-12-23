'''def fib(n):
    if n<0:
        print('Incorrect')
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

n=10
print(fib(n))'''

#dynamic appraoch
def fib(n):
    f=[0,1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

n=10
print(fib(n))