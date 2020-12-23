class demo:
    print('Hello I am inside my class')
    def funcn(self, a,b): #method
        return 100


obj=demo() #object/instance of a class
res=obj.funcn(10, 20) 
print(res)