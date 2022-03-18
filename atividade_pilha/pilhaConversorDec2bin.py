import os
class Pilha:
    def __init__(self):
        self._vet = [] # lista interna

    def peek(self): # retorna qual item esta no topo
        return self._vet[-1]
       
    def push(self, item): # metodo de inserir item
        self._vet.append(item)
        
    def pop(self): # remover o topo e retornar item para usuario
        # tratar caso de underflow
        if self.is_empty():
            print("Lista Vazia!")
            return None
        return self._vet.pop()
                
    def is_empty(self): # teste se é vazia
        if len(self._vet) > 0:
            return False
        return True
        
    def __len__(self): # retorna o total de itens
        return len(self._vet)

    def __str__(self): # representacao da pilha como string
        return str(self._vet)

## Objetivo 1: Converter Decimal para Binário

def decimal_binario():
    p1 = Pilha()
    numero = int(input('Digite um numero decimal: '))
    while numero > 0:
        p1.push(numero % 2)
        numero = numero // 2
    print('O numero binario é: ', end='')
    while not p1.is_empty():
        print(p1.pop(), end='')
    print()
    os.system('pause')

if __name__ == "__main__":
    decimal_binario()




     



    

