from lse import *

#push pop peek __len__
class PilhaEncadeada:
    def __init__(self):
        self.lista = LSE()
    
    def __len__(self):
        return len(self.lista)

    def push(self, item):
        if self.lista.head is None:
            self.lista.inserir_inicio(Nodo(item))
        
    def pop(self):
        if len(self) > 0:
            return self.lista.remover_inicio()
        else:
            return None

    def peek(self):
        if self.lista.head is None:
            return None
        else:
            return self.lista.head.dado
