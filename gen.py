'''def mul(l=[]):
    for i in range(len(l)):
        if l[i]%2==0:
            print(l[i])

mul([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20])'''
'''
def demo_gen():
    n=1
    print('This is line no. 1')
    yield(n)
    n=n+1 # 1+1
    print('This is line no. 2')
    yield(n) #2
    n=n+1
    print('line 3')
    yield(n)

res=demo_gen() #calling function
print(type(res)) #getting the type of my function
for i in res:
    print(i)'''

'''
def seq():
    num=0
    while num<10:
        yield num
        num=num+1

for i in seq():
    print(i)
'''
'''
def reverse_str(test_str):
    length = len(test_str)
    for i in range(length-1, -1, -1):
        yield test_str[i]

for char in reverse_str('Consultadd'):
    print(char)'''












