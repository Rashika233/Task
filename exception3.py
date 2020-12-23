'''
x=-1
if x<0:
    raise Exception('Sorry, we cannot accept values less than 0')'''

x='consultadd'
if not type(x) is int:
    raise TypeError('Only integers are accepted')