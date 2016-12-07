print "Conversor de segundos a dias,horas y minutos"
def tiempo(s):
    dias=(s//86400)
    horas=(s%86400//3600)
    minutos=(s%3600//60)
    segundos=(s%60)
    print(dias, "dias")
    print(horas, "horas")
    print(minutos, "minutos")
    print(segundos, "segundos")
#Luis Manuel Garcia Valdivia

