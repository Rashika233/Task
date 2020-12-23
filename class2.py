class demo2:
    def __init__(self,a):
        self.a='alpha'

    def first(self):
        print('Hello I am a method here')

    def second(self):
        print('Hello I am second method')
d=demo2(10)
res=d.first()
res2=d.second()
print(d)
print(res)
print(res2)
