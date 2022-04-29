import csv

tabela_periodica = {}
estados = {'l': 'Líquido', 'g': 'Gasoso', 's': 'Solido'} 

arq = csv.reader(open('tabela.csv'), delimiter=';')
for i,dado_linha in enumerate(arq):
    if i == 0: 
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] 
    dados['nome'] = dado_linha[1] 
    dados['numeroAtomico'] = dado_linha[2] 
    dados['linha'] = dado_linha[3] 
    dados['coluna'] = dado_linha[4] 
   
    
    tabela_periodica[dados['simbolo']] = dados

print('''
                                MENU:

        [1] - Listar todos os dados de todos os elementos inseridos
        [2] - Listar todos os dados de determinado elemento, buscando através do seu nome
        [3] - Listar dados de determinado elemento, buscando através do seu símbolo
        [s] - Sair
    ''')

def teste():
    
        resp = int(input('Qual das opções acima você vai escolher: '))
            
        if resp == 1:
            print([tabela_periodica])
            
        

        if resp == 3:
                simbolo = input('Qual o símbolo do elemento: ')
                if simbolo in tabela_periodica:
                    print(tabela_periodica[simbolo])
                    
                else:
                    print('Elemento não encontrado')
                    
        if resp == 2:  
            print('''
                    MENU:
                        [1] - Mercurio
                        [2] - Carbono 
                        [3] - Calcio
                        [4] - Oxigenio
                        [5] - Cobre
                    ''')
            op = input('Escolha uma opção: ')

            if op == '1':
                for linha in tabela_periodica.values():
                    if linha['nome'] == 'Mercurio':
                        print(linha)
            if op == '2':
                for linha in tabela_periodica.values():
                    if linha['nome'] == 'Carbono':
                        print(linha)
            elif op == '3':
                for linha in tabela_periodica.values():
                    if linha['nome'] == 'Calcio':
                        print(linha)
            elif op == '4':
                for linha in tabela_periodica.values():
                    if linha['nome'] == 'Oxigenio':
                        print(linha)
            elif op == '5':
                for linha in tabela_periodica.values():
                    if linha['nome'] == 'Cobre':
                        print(linha)
            else:
                print('Opção inválida')
            



teste()














    
    
