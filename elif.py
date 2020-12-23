#syntax--

'''if test expression:
        statements
    elif test expression:--> else + if
        statements

    else:
        body of else'''


a=190
if a%19==0:
    print('the value of a is the multiple of 19')

if a<200:
    print('the value of a is less than 200')

elif a==100: #whether the value of a is not equal to 100
    print('the value of a is not equivalent to 100')

else:
    print('the value of a is :', a)