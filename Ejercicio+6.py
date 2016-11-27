

print "Calculo del indice de masa corporal"
def imc(x,y):
    imc=x//y**2
    print imc
    
    if imc<16.00:
      print "Delgadez severa"
    elif imc<99 and imc>16:
      print "Delgadez moderada"
    elif imc>17 and imc <=18.40:
      print "Delgadez leve"
    elif imc>18.50 and imc <25:
      print "Normal"
    elif imc>25 and imc <29:
      print "Sobrepeso"
    elif imc>30 and imc <39:
      print "Obesidad"
    else:
      print "Obesidad morbida"

