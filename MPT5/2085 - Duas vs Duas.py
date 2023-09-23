cartaum_dum = int(input())
cartaum_ddois = int(input())
cartadois_dum = int(input())
cartadois_ddois = int(input())
ponto_dum = 0
ponto_ddois = 0

if cartaum_dum> cartadois_dum:
  ponto_dum = cartaum_dum
else:
  ponto_dum = cartadois_dum

if cartaum_ddois> cartadois_ddois:
  ponto_ddois = cartaum_ddois
else:
  ponto_ddois = cartadois_ddois

if ponto_dum == ponto_ddois:
  print('empate')
elif (ponto_ddois > ponto_dum):
  print (ponto_ddois)
else:
  print(ponto_dum)
