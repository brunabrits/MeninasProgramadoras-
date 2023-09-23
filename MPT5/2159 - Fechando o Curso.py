nome = input()
aula = int(input())
tarefas_um = int(input())
tarefas_dois = int(input())
tarefas_tres = int(input())
monitorias_um = int(input())  
monitorias_dois = int(input())
monitorias_tres =  int(input())
avaliacao = float(input())

if aula >= 2 and (tarefas_um >=75 ) and (tarefas_dois >= 75) and (tarefas_tres >= 75) and (monitorias_um == 1) and (monitorias_tres ==1) and (monitorias_dois == 1) and (avaliacao >=5 ):
      print(nome, 'aprovada')
else:
          print (nome, 'reprovada')
