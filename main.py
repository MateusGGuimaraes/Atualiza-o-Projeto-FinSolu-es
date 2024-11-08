import json
import os
import cadastro
import perfil
import investimento  

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

def menu():
    while True:
        print(f"-----> {cor.AZUL}Sistema FinSoluções{cor.RESET} <-----")
        print("1 - Módulo Usuários")
        print("2 - Perfil Financeiro")
        print("3 - Módulo Investimento")
        print("0 - Sair")

        opcao = int(input("Escolha uma das opções acima: "))

        if opcao == 1:
            cadastro.menu()  
            continue
        elif opcao == 2:
            perfil.menu()  
            continue
        elif opcao == 3:
            investimento.menu_investimentos()  
            continue
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print(cor.VERMELHO + "Opção inválida! Tente novamente." + cor.RESET)

menu()
