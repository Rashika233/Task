x=int(input('Enter the value'))

if x==10:
    print('The user has given 10 value')

if x<=5: #if this condition will be true
    print('User has given either less than or equals to 5')

    if x==2: 
        print('the exact value is 2')
    else:
        print('We don"t know the exact value')

if x%3==0:
    print('the value is divisible by 3')
else:
    print('The value of x is:', x)