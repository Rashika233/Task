test_list = [6, 4, 8, 9, 10,False,[],{},] 
 
 
 
res = [ False if bool(test_list[x])==False else True for x in range(len(test_list))]
print (res)
 