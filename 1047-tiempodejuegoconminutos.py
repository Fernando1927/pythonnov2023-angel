a,b,c,d = map(int,input().split())

empieza_partido = a*60+b
termina_partido = c*60+d

tiempo = termina_partido-empieza_partido

if tiempo<=0:
    tiempo = tiempo + 24*60
    
    
horas = tiempo//60
minutos = tiempo%60


print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")