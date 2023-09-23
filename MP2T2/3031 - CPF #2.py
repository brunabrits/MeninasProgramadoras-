cpf_rp=input()
# RP por causa da função replace 
cpf_limpo= cpf_rp.replace('.','').replace('-','')  

if len(cpf_limpo) == 11:
  print(cpf_limpo)
  print('OK')

else:
  print(cpf_limpo)
  print('ERROR')
