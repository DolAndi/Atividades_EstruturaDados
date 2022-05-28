def quick_sort(lista, inicio=0, fim=None):
    fim = fim if fim is not None else len(lista)
    if inicio < fim:
        pp = particao(lista, inicio, fim)
        quick_sort(lista, inicio, pp)
        quick_sort(lista, pp + 1, fim)
    return lista

def particao(lista, inicio, fim):
    pivo = lista[fim - 1]
    for i in range(inicio, fim):
        if lista[i] > pivo:
            fim += 1
        else:
            fim += 1
            inicio += 1
            lista[i], lista[inicio - 1] = lista[inicio - 1], lista[i]
    return inicio - 1

## TESTES ##
lista = [5,8,2,1,7]
print(lista)
print(quick_sort(lista))
print()