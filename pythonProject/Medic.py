Pacientes = []

opciones_menu = ['Añadir paciente','eliminar Paciente','Consultar paciente']

print(opciones_menu)
print("Que opcion quieres")

opcion = input()
opcion = int(opcion)

# Añadir paciente
if opcion == 1:
    nombre = input("Nombre del Paciente: ")
    apellido = input("Apellido del Paciente: ")
    edad = input("edad del Paciente: ")
    enfermedad = input("enfermedad del Paciente: ")
    paciente = {'Nombre':nombre,'Apellido':apellido,'edad':edad,'Enfermedad':enfermedad}
    Pacientes.append(paciente)
    print("El paciente se ha Añadido con exito")
    print(Pacientes)

if opcion == 2:
    nombre = input('Nombre del paciente')
    Pacientes.pop('nombre'==nombre)
    print(Pacientes)