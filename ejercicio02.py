print("Generador de listas")

numero_listas = list(range(int(input("¿Cuántas listas quiere escribir? "))))
sub_lista = list()
lista = numero_listas

for x in numero_listas:
    palabras_lista = list(range(int(input(f"Digame cuantas palabras tiene la lista {x+1}: "))))
    for y in palabras_lista:
        sub_lista.append(input(f"Digame la palabra {y + 1}: "))
        if y+1 == len(palabras_lista):
            lista[x] = sub_lista[(-len(palabras_lista)):]


for x in numero_listas:
    print("La lista {} es: {}".format(numero_listas.index(x) + 1, lista[numero_listas.index(x)]))