numero = int(input())
chute = int(input())
  
while numero != chute :  
  if chute > numero :
    print ('maior')
  
  elif chute < numero:
    print('menor')
    
  chute = int(input())
  
if numero == chute:
  print('igual')
