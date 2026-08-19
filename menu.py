from utilidades import *
from validacoes import *

def menu():
    while True:
        print("\33[34m===============\033[m")
        print("Selecione o que você gostaria de fazer:")
        escolha = input(" | 0 - Sair \n | 1 - Informações sobre a sustentabilidade \n | 2 - Solução de problemas\n | Escreva aqui: ").replace(" ", "")
        print("\33[34m===============\033[m")

        match escolha:
            case "0":
                print ("Você saiu")               
                break

            case "1":
                informacoes()

            case "2":
                solucao_problemas()

            case _:
                erro()
                continue
