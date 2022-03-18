class Fila:    
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item): # enfileirar
        self._vet.append(item)
    
    def dequeue(self): # desenfileirar
        if len(self._vet) > 0:
            return self._vet.pop(0)
        else:
            raise Exception("Fila Vazia")

    def front(self): # mostrar o 1o da fila, sem remover!
        return self._vet[0]
                
    def is_empty(self): # retorna se a fila esta vazia
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): # representacao da fila como string
        return str(self._vet)

## Filas - Painel de Atendimento

if __name__ == "__main__":
    # Criando uma Fila
    f = Fila()
    senha = 0
    lista_chamados = []
    while True:
        print(
         "1) Obter nova senha\n"
         "2) Chamar próxima senha\n"
         "3) Mostrar senhas chamadas\n"
         "0) Encerrar o programa\n")
        decisao = int(input("Escolha uma opção: \n" ))
        if decisao == 1:
            f.enqueue(senha)
            senha += 1
        elif decisao == 2:
            if f.is_empty():
                print("É necessário obter uma senha primeiramente. Acesse a opção (1)")
            else:
                senha = f.front()
                lista_chamados.append(senha)
                f.dequeue()
                print("A próxima senha será: ", senha)
        elif decisao == 3:
            if len(lista_chamados) == 0:
                print("Não foi possível, nenhuma senha foi chamada")
            else:
                print("As últimas senhas chamadas foram: ", lista_chamados)
        elif decisao == 0:
            print("Obrigado! Volte ainda!")
            break
        else:
            print("Opção inválida! Encerrando...")
            break
