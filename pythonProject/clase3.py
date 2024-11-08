# parte 1 - Index
mi_frase = "Hola mundo"

#Encontrar la primera ocurrencia
resultado = mi_frase.index("o")
# buscar de derecha a izquierda la primera ocurrencia
resultado2 = mi_frase.rindex("o")

print(resultado)
print(resultado2)

# parte 2 - substrings

print(mi_frase[::2])

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

