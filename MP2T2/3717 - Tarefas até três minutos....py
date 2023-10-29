def tarefas(linha,tarefa_curta,tarefa_longa):
    while linha !='.':
      tempo,tarefa= linha.split(" ",1)
      tempo=int(tempo)
  
      if tempo <= 3:
        tarefa_curta.append(tarefa)
      else:
        tarefa_longa.append(tarefa)

      linha=input()

    [print('Fazer agora a tarefa:', tarefa) for tarefa in tarefa_curta]
    print(tarefa_longa)


linha=input()
tarefa_curta=[]
tarefa_longa=[]

tarefas(linha,tarefa_curta,tarefa_longa)
