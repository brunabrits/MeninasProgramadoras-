status=input()
acertos = 0 
while status != 'timeout':
    if status =='accepted':
        acertos +=1
    status=input()   
    
        
print(acertos)
