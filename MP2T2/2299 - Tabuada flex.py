meio=int(input())
comeco=int(input())
fim=int(input())

print('Tabuada do',meio,'de',comeco,'até',fim)

for num in range(comeco,fim+1,1):
  tab= num * meio  
  print(meio,'x',num,'=',tab)
