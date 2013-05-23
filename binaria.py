def busqueda_binaria(a,valor,inicio,final):
    mitad=int((inicio+final)//2)
    if a[mitad] == valor:
        return '%s %s' %('Ersitoo!! , el numero se encuentra en la posicion ',mitad)
    elif inicio > final or valor > a[-1]:
        return '%s' %('Lo siento, el numero no se encuentra')
    elif a[mitad] < valor:
        return busqueda_binaria(a,valor,mitad+1,final)
    else:
        return busqueda_binaria(a,valor,inicio,mitad-1)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
inicio=0
final=len(a)
