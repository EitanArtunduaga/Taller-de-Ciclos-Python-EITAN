puntos=[10,9,-1,8,-100,10]
total=0


for punto in puntos:
    if punto<0:
        continue
    print("ganaste " ,punto, " puntos")
    total += punto

print("total de puntos ganados: ", total)
