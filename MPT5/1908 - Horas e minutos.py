minuto = int(input())
if  (minuto > 59):
  minutos = minuto % 60 
  horas =  '{:.0f}'.format((minuto - minutos) /60 )
 
  print (minuto,'minutos =',horas,'horas e',minutos, 'minutos')
  
else:
  print (minuto,'minutos = 0 horas e', minuto,'minutos')    
