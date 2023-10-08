vela=int(input())
contagem_sopro = 0 
while contagem_sopro < vela:
    sopro=input()
    if sopro == 'fuuuuuuu':
        print('bom sopro!')
        contagem_sopro +=1
        
    elif sopro == 'fuuu':
        print('um pouco mais de força no sopro!')
        
    elif sopro == 'fu':
        print('precisa de muito mais força no sopro!')
        
print('Parabéns para pelo seu aniversário de {} anos!'.format(vela))
