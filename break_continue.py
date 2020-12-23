while True:
    x=int(input('Enter the value')) 


    if x==5:
        print('Hello according to the code I am at line 6')
        break #break tries to terminate the loop
        print('Hello I am at line no 7')
    
    if x==10:
        print('I am at line no 10')
        continue #tries to forcefully continue the next iteration by throwing the control back to the wile loop
        print('Condition after continue statement')

print('Hence done')