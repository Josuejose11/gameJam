
import validacoes
from utilidades import *
from validacoes import *
from menu import *
from datetime import *
import pwinput

print("Seja bem vindo ao nosso sistema!")
print ("Nossa missão é ajudar empresas a encontrar soluções sustentáveis para os desafios do presente e construir um futuro melhor!")

while True:
    escolha = input("Escolha uma das opões:\n | 0 - Sair \n | 1 - Entrar \n | 2 - Criar login\n | Escreva aqui: ").strip()

    if escolha.strip() == "":
        print("Campo vazio!")
        continue

    match escolha:
        case "0":
            print ("Você saiu")               
            break

        # login do usuario 
        case "1":
            if not ler_usuarios():
                continue

            print("===============")
            id_usuario = validar_id()
            escolha = input("Você deseja visualizar a sua senha enquanto digita?\n | 1 - Sim\n | 2 - Não\n | Digite aqui: ").replace(" ", "")

            if escolha == "1":
                senha = input("Digite sua senha: ")
            elif escolha == "2":
                senha = pwinput.pwinput("Digite sua senha: ", mask="*").strip()
            else:
                erro()
                continue
            
            print("\33[31m===============\033[m") 

            if not entrar(id_usuario, senha):
                continue

            menu()

        # Criação da conta do usuario
        case "2":                       
                print ("\33[34m===============\033[m")
                
                #nome
                while True:
                    nomeInicial = input("Digite o nome de sua empresa: ").strip().capitalize()

                    nome = validar_nome(nomeInicial)

                    if not nome:
                        erro()
                        print("Preencha o campo corretamente")
                        continue

                    break
                
                #email
                while True:
                    email = input("Digite a seu email: ").replace(" ", "")
                    if not validar_email(email):
                        continue
                    break
                
                #senha
                senha = validar_senha()

                print("\33[31m===============\033[m")  
                
                criar_login(nome, email, senha)

                denovo()

        case _:
            erro()
            print("Escolha uma das opções! :(")
            continue

        