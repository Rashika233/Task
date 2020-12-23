try:
    print('We are inside our try block')
    x=int(input('Enter the 1st no'))
    y=int(input('Enter the 2nd no'))
    res=x/y
    print(res)

except ZeroDivisionError:
    print('We are inside our except block')
    print('you are trying to divide your 1st no with 0')

else:
    print('We are inside our else block')
finally:
    print('We are inside our finally block')
