ano_um=int(input())
taxa_um=float(input())
ano_dois=int(input())
taxa_dois=float(input())

if taxa_um > taxa_dois:
    print(ano_um)
elif taxa_dois > taxa_um:
    print(ano_dois)
elif taxa_um ==taxa_dois:
    print('iguais')
