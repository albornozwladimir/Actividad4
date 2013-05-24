def busqueda_binaria_i(a, Val, inicio, final):
    while inicio < final:
        mitad = (inicio+final)//2
        midval = a[mitad]
        if midval < Val:
            inicio = mitad+1
        elif midval > Val:
            final = mitad
        else:
            return '%s %s' %('Ersitoo!! , el numero se encuentra en la posicion ',mitad)
    return '%s' %('Lo siento, el numero no se encuentra')

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
inicio = 0
final = len(a)


