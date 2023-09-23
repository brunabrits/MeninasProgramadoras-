n = int(input())
fisica = 0
juridica = 0
for i in range (n):
  
  pessoa = input()
  valor = float(input())
  if pessoa =='F':
    somando_f= ((valor /100 *6))
    fisica +=somando_f
  elif pessoa == 'J':
    somando_j= ((valor /100 *1))
    juridica +=somando_j
    
print('{:.2f}'.format(fisica))
print('{:.2f}'.format(juridica))
