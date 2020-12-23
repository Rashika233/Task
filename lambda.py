#syntax:
#lambda arguments: expression
'''1) filter()
2) map()
3) reduce()'''
#case1
#double=lambda var: var*var #var--> argument, var*var--> expression
#print(double(10))


#case2
'''list1=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
new_list=list(filter(lambda x: (x%2==0), list1))
print(new_list)'''
'''
def mul(l=[]):
    for i in range(len(l)):
        if l[i]%2==0:
            print(l[i])

mul([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20])'''
#case 3
#l=[1,2,3,4,5,6,7]

'''def mul(l=[]):
    for i in range(len(l)):
        l[i] = l[i]*l[i]
        print(l[i])

mul([1,2,3,4,5,6,7])'''
'''
l=[1,2,3,4,5,6,7]
res=list(map(lambda i: (i*i), l))
print(res)'''

#syntax:

#reduce(function(lambda), seq)
'''
import functools
res=functools.reduce(lambda x, y: x*y, [1,2,3,4,5,6,7,8])
print(res)'''

from functools import reduce
res=reduce(lambda x, y: x+y, [1,2,3,4])