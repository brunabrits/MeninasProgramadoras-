cartinha= input()
cartinha_2= input()
cartinha_3= input()

conte=0

# 7COPAS
if cartinha  == '7Copas':
    conte= conte+1
    
if  cartinha_2 == '7Copas':
    conte= conte+1
    
if  cartinha_3 == '7Copas':
    conte= conte+1

#4PAUS

if cartinha  == '4Paus':
    conte= conte+1
else:
    conte = conte+0
    
if  cartinha_2 == '4Paus':
    conte= conte+1
else:
    conte = conte+0
    
if  cartinha_3 == '4Paus':
    conte= conte+1
else:
    conte = conte+0
    

#AESPADA

if cartinha  == 'AEspadas':
    conte= conte+1
else:
    conte = conte+0
    
if  cartinha_2 == 'AEspadas':
    conte= conte+1
else:
    conte = conte+0
    
if  cartinha_3 == 'AEspadas':
    conte= conte+1
else:
    conte = conte+0


#7Ouros

if cartinha  == '7Ouros':
    conte= conte+1
else:
    conte = conte+0
    
if  cartinha_2 == '7Ouros':
    conte= conte+1
else:
    conte = conte+0
    
if  cartinha_3 == '7Ouros':
    conte= conte+1

else:
    conte = conte+0

print(conte)
