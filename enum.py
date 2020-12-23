'''l1=['eat', 'sleep', 'repeat']
for ele in enumerate(l1):
    print(ele)'''
'''
l1=['eat', 'sleep', 'repeat']
for count, ele in enumerate(l1, 100):
    print(count, ele)'''

Traceback (most recent call last):
  File "enum.py", line 6, in <module>
    for count, ele in enumerate(l1, 100):
NameError: name 'l1' is not defined