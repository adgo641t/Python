# parte 1 - Index
mi_frase = "Hola mundo"

#Encontrar la primera ocurrencia
resultado = mi_frase.index("o")
# buscar de derecha a izquierda la primera ocurrencia
resultado2 = mi_frase.rindex("o")

print(resultado)
print(resultado2)
#-----------------------------------------------------#

# parte 2 - substrings

print(mi_frase[::2])
#-----------------------------------------------------#

# parte 3 - metodos strings

# Upper - Mayusculas
# lower - Minusculas
# split - Separarlo en partes
# join  - unir
# find  - encontrar cadenas

a = 'Hola soy '
b = 'Adrian'
c = ''.join([a,b])

print(mi_frase.upper())
print(mi_frase.lower())
print(mi_frase.split())
print(c)
print(mi_frase.find('mundo'))
#-----------------------------------------------------#

# parte 4 - Propiedades de los strings

nombre1 = 'kari'
nombre2 = 'na'
nombreraro = 'hola \n que \n tal'

print(nombre1+nombre2)
print(nombreraro)

# encontrar palabras
print("que" in nombreraro)

# Encontrar palabras que no esta
print("que" not in nombreraro)

#Longitud
print(len(nombreraro))
#-----------------------------------------------------#
# parte 5 - Listas

listaNum = [1,2,3,4,5]
lista = ['Pepe','Adrian','Martin']

# sumar listas
print(listaNum + lista)

# longitud de lista
print(len(lista))

# añadir a la lista
listaNum.append(6)
print(listaNum)

# eliminar una cosa de la lista por indice
#listaNum.pop(6)
print(listaNum)

# ordenar la lista
listaNum = [8,2,4,6,7,1,9]
listaNum.sort()
print(listaNum)

# Nos da la lista al reves
listaNum.reverse()
print(listaNum)
#---------------------------------------------------#
# Parte 5 - Diccionario

dic = {'nombre':'Alejandro','apellido':'Hernandez','edad':20}
# Añadir datos con lista en el diccionario
dic['caracteristicas'] = ['alto','moreno']
print(dic['apellido'])

#para buscar dentro de una lista en el diccionario
print(dic['caracteristicas'][1])


