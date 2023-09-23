time_um =0
time_dois=0
final_do_set= False


while not final_do_set:
  pontuacao = int(input())
  if pontuacao == 1:
    time_um += 1 
  else:
    time_dois += 1

  diferentin = time_um - time_dois
  if diferentin < 0: 
    diferentin = -diferentin

  if time_um > time_dois:
    ganhando = time_um
  else:
    ganhando = time_dois 
  
  if ganhando >= 25 and diferentin >= 2:
    final_do_set = True
    print (time_um,'x',time_dois)
