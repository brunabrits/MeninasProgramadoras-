n_votos = int(input())
X = 0
Y = 0
B = 0
N = 0

for i in range(n_votos):
  voto = input()
  if voto =='X':
   X += 1

  if voto =='Y':
    Y += 1

  if voto =='B':
   B += 1

  if voto =='N':
   N += 1

print('X',X)
print('Y',Y)
print ('Brancos e nulos',B+N )

if X > Y:
  print('vitoria: X')
elif X < Y: 
  print('vitoria: Y')
elif X == Y: 
  print('empate!')
