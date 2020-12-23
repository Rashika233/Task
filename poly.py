#for any in-built funcn
'''
print(len('Rashika'))

print(len([1,2,3]))'''

#for user defined func
'''def add(x,y,z=0):
return x+ y+z

print(add(2,3))
print(add(3,4,5))'''

#with class method

class India():
    def capital(self):
        print('India')
    def language(self):
        print('Hindi')
    def type(self):
        print('developing')

class USA:
    def capital(self):
        print('Washington DC')
    def language(self):
        print('English')
    def type(self):
        print('Developed')

obj_india=India()
obj_usa=USA()
for country in (obj_india,obj_usa):
    country.capital()
    country.language()
    country.type()