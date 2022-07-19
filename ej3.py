print("Datos de personas")

numero_personas = list(range(int(input("Número de personas: "))))
sub_lista = list()
lista = numero_personas
print("Ingrese el nombre,dni y edad respectivamente")

for x in numero_personas:
    personas_lista = list(range(3))
    for y in personas_lista:
        sub_lista.append(input(f"Ingrese dato {y + 1}: "))
        if y+1 == len(personas_lista):
            lista[x] = sub_lista[(-len(personas_lista)):]


for x in numero_personas:
    print("La persona {} es: nombre, dni, edad{}".format(numero_personas.index(x) + 1, lista[numero_personas.index(x)]))


