

print ("Intereses anuales")
interes=0.04
saldoinicial=float(input("Cantidad a depositar"))
def funcion(x):
  x=(x*0.04)+x
  return x
for i in range(0,4):
  saldoinicial=funcion(saldoinicial)
  print funcion(saldoinicial)
  #Luis Manuel Garcia Valdivia
