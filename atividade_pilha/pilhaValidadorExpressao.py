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
#============================================================================================
## Objetivo 2: Validador de Expressões
#============================================================================================
if __name__ == "__main__":
    #Validador de expressao
    p1 = Pilha()
    expressaoIn = input("Digite a expressao: ")
    expressao = expressaoIn.split()
    for i in expressao:
        if i == '{' or i == '[' or i == '(' :
            p1.push(i)
        elif i == '}' or i == ']' or i == ')':
            if p1.is_empty():
                print("Expressao invalida!")
                break
            else:
                if i == '}' and p1.peek() == '{':
                    p1.pop()
                elif i == ']' and p1.peek() == '[':
                    p1.pop()
                elif i == ')' and p1.peek() == '(':
                    p1.pop()
                else:
                    print("Expressao invalida!")
                    break
                if p1.is_empty():
                    print("Expressao valida!")
                    break
  