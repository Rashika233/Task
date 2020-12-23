answer = input("Enter a string: ")
vowel_repeated_count = 0

length_Answer = len(answer)
i=0
while (i <length_Answer-1):
    #we check if it's a vowel
    if answer[i] in ["a","e","i","o","u"]:
        #we check if it's followed by the same vowel
        if answer[i+1] == answer[i]:
            #increment the vowel_repeated_count
            vowel_repeated_count   +=1
            #we save the vowel for the display
            vowel = answer[i]
            #we skip the other same repeated vowels 
            #example: abceeed, we skip the third e
            while (answer[i] == vowel and i < length_Answer-1):
                i +=1
        #we add this incrementation because we're in a while loop
        i +=1


if vowel_repeated_count == 0:
    print("no repeating vowles")
elif vowel_repeated_count == 2:
    print("the letter "+ str(vowel) +" repeats")
else:
    print ("more than 1 repeating vowels")
