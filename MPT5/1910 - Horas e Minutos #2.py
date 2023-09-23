quantidade_de_vezes = int(input())
i = 1 

for i in range (quantidade_de_vezes):
  minuto = int(input())
  horas = minuto // 60
  minutos = minuto % 60 
  print('{:02d}''h''{:02d}''min'.format(horas,minutos))
