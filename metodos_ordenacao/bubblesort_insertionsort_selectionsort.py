## Criacao dos metodos de ordenacao

def bubble_sort(lista):
    troca = True
    while troca == True:
        troca = False
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                troca = True
    return lista

def insertion_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, i):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def menor(lista, inicio=0): # retorna o indice com o menor valor
    menor = inicio
    for i in range(inicio, len(lista)):
        if lista[i] < lista[menor]:
            menor = i
    return menor

def selection_sort(lista):
    for i in range(0, len(lista)):
        indice_menor = menor(lista, i)
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    return lista
    
## TESTES ##
lista = [5,8,2,1,7]
print(lista)
print(bubble_sort(lista))
print()

lista = [5,8,2,1,7]
print(lista)
print(insertion_sort(lista))
print()

lista = [5,8,2,1,7]
print(lista)
print(selection_sort(lista))