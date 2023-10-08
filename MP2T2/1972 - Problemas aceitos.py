status=input()
ac1= 'No'
ac2= 'No'
ac3= 'No'
ac4= 'No'
while status != 'timeout':
    if status =='accepted 1':
        ac1 = 'Yes'
        
    if status =='accepted 2':
        ac2 = 'Yes'
        
    if status =='accepted 3':
        ac3 = 'Yes'
   
    if status =='accepted 4':
        ac4 = 'Yes'
   
    status=input()   

print(ac1,ac2,ac3,ac4)
        
