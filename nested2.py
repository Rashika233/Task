y=100 #i'm having the value of my y variable as 100

if y==120: #100==120 ---> false
    print('The value is equivalent to 120')

if False: #---> false condition
    print('Hello I am a false value')
    if True: #---> true condition
        print('Hello I am inside line no 9.')
    else: 
        print('The else part of the code will only get executed iff the above logic is false')

else:
    print('The value of y is equivalent to 100')