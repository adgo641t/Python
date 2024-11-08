pais ='españa'
pais2 = 'portugal'
print("Tu eres de " +pais +" y tu comapñero es de "+pais2)

num1 = 550
num2 = 105

print (num1 + num2)

num1 = -10
num2 = 4

suma_numeros = num1 + num2

print(suma_numeros)
print(type(suma_numeros))

edad = input('dime tu edad: ')


num1 = 5.8
print(num1)

num2 = int(num1)
print(num2)


color_coche ="Rojo"
matricula_coche = 5678
print("mi auto es {} y de matricula {}".format(color_coche,matricula_coche))

x = 10
y = 5
print("Mis numeros son: "+str(x)+ " y "+ str(y))
print("Mis numeros son {} y {} y la suma es: {}".format(x,y,x+y))
print(f"el coche es de {color_coche} y su matricula es {matricula_coche}")

resultado = 90/7
print(resultado)
print(round(resultado,2))

comision = 13
nombre = input("Cual es tu nombre: ")
vendidos = input("Cuanto has vendido: ")
ventas_totales = int(vendidos)
dinero_percibido = round(ventas_totales * (comision /100))
print(f'{nombre} te pertenece {dinero_percibido}')