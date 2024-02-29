entrada=input()
dicionario={}
while entrada != "fim":
    chave,valor=entrada.split()
    valor = int(valor)
    dicionario[chave]=valor
    print(dicionario)
    entrada=input()

# ideia aplicada atráves do exercicio tarefas até 3 min da semana 7 onde recebemos
