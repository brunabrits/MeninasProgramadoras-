face_um =[int(i) for i in input().split()]
face_dois = [int(i) for i in input().split()]
face_tres =  [int(i) for i in input().split()]

soma_um = face_um.count(1)
soma_dois = face_dois.count(1)
soma_tres = face_tres.count(1)

print(soma_um + soma_dois + soma_tres)
