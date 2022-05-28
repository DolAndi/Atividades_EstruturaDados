def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        listaEsquerda = lista[:meio]
        listaDireita = lista[meio:]
        mergeSort(listaEsquerda)
        mergeSort(listaDireita)
        i = 0
        j = 0
        k = 0
        while i < len(listaEsquerda) and j < len(listaDireita):
            if listaEsquerda[i] < listaDireita[j]:
                lista[k]=listaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDireita[j]
                j += 1
            k += 1
        while i < len(listaEsquerda):
            lista[k]=listaEsquerda[i]
            i += 1
            k += 1
        while j < len(listaDireita):
            lista[k]=listaDireita[j]
            j += 1
            k += 1
    return lista

## TESTES ##
lista = [5,8,2,1,7]
print(lista)
print(mergeSort(lista))
print()