MINIMUM= 32
  
def find_minrun(n): 
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 
  
def insertion_sort(lista, esquerda, direita): 
    for i in range(esquerda+1,direita+1):
        element = lista[i]
        j = i-1
        while element<lista[j] and j>=esquerda :
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = element
    return lista
              
def merge(lista, l, m, r): 
    lista_tam1 = m - l + 1
    lista_tam2 = r - m 
    esquerda = []
    direita = []
    for i in range(0, lista_tam1): 
        esquerda.append(lista[l + i]) 
    for i in range(0, lista_tam2): 
        direita.append(lista[m + 1 + i]) 
    i=0
    j=0
    k=l
    while j < lista_tam2 and  i < lista_tam1: 
        if esquerda[i] <= direita[j]: 
            lista[k] = esquerda[i] 
            i += 1
        else: 
            lista[k] = direita[j] 
            j += 1
        k += 1
    while i < lista_tam1: 
        lista[k] = esquerda[i] 
        k += 1
        i += 1
    while j < lista_tam2: 
        lista[k] = direita[j] 
        k += 1
        j += 1
  
def tim_sort(lista): 
    n = len(lista) 
    minrun = find_minrun(n) 
    for comeco in range(0, n, minrun): 
        fim = min(comeco + minrun - 1, n - 1) 
        insertion_sort(lista, comeco, fim) 
    size = minrun 
    while size < n: 
        for esquerda in range(0, n, 2 * size): 
            mid = min(n - 1, esquerda + size - 1) 
            direita = min((esquerda + 2 * size - 1), (n - 1)) 
            merge(lista, esquerda, mid, direita) 
  
        size = 2 * size 

## TESTES ##
lista = [-1,5,0,-3,11,9,-2,7,0] 
print(lista) 
tim_sort(lista) 
print(lista)
print()