def selection_sort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

lista = [64, 25, 12, 22, 11]
print("Lista original:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)
