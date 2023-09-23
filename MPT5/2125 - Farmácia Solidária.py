data_atual=[int(i) for i in input().split()]
val_remedio=[int(i) for i in input().split()]

if ((data_atual[0]) > (val_remedio[0])) and ((data_atual[1]) >= (val_remedio[1])) and ((data_atual[2]) >= (val_remedio[2])):
  print('vencido!')
  
elif ((data_atual[2]) < (val_remedio[2])):
  print('na validade')

elif ((data_atual[1]) < (val_remedio[1])) and ((data_atual[2]) == (val_remedio[2])):
  print('vence este ano')

elif (data_atual[1]) == (val_remedio[1]) and (data_atual[2]) == (val_remedio[2]):
  print('vence este mês')

# 04 09 2004  
# 0   1   2
