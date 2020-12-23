inp_str = input('Enter the string:')
str_low = inp_str.lower()
vowels = 'aeiou'
count = 0

for i in (str_low):
    
    if i in vowels:
        count = count+1
        print(i)
       
print('Vowel count in the given string is:', count)