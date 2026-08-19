from google import genai
from google.genai import types
import time
import threading  

# def Nenhuma das opções anteriores  
def nenhuma_das_opcoes(texto = None):
    print ("---------------")
    prompt = input("Fale para a nossa IA sobre o seu problema para que nós possamos te ajudar\nQual o problema presente na sua empresa: ")
    Ia(texto + prompt)

#def de "Pensando..." 
def carregando():
    pensando = True
    
    thread = threading.Thread(target=carregando)
    thread.start()

    while pensando:

        print("\rPensando   ", end="", flush=True)
        time.sleep(0.5)

        print("\rPensando.  ", end="", flush=True)
        time.sleep(0.5)

        print("\rPensando.. ", end="", flush=True)
        time.sleep(0.5)

        print("\rPensando...", end="", flush=True)
        time.sleep(0.5)

# Def da conexao e conversa c o gemini
def gemini(texto):
    

    resposta  = "Me dê apenas uma resposta simples para: " + texto
    client = genai.Client(api_key="Sua chave de API do Gemini aqui")  # Substitua pelo seu token de API do Gemini

    config = types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Chat: "+texto,
        config=config
    )

    resposta = response.text
    pensando = False
    thread.join()
    


    print ("\n\nChat: " + resposta)

#  def de inicio da conversa c a ia
def Ia(msg):
    global pensando

    pensando = True
    thread = threading.Thread(target=carregando)
    thread.start()

    resposta = gemini(msg)

    pensando = False
    thread.join()
    print ("\n\nChat: " + resposta)
    print ("---------------")
    while True:
        escolha = input("Essa resposta foi útil para você? \n | 1 - Sim \n | 2 - Não \n | Digite aqui: ")
        match escolha:
            case "1":
                print("Fico feliz em ter ajudado! Se precisar de mais alguma coisa, estou à disposição.")
                break
            case "2":
                escolha = input("Gostaria de tentar novamente? \n | 1 - Sim \n | 2 - Não \n | Digite aqui: ")
                match escolha:
                    case "1":
                        nenhuma_das_opcoes()
                    case "2":
                        break
            case _:
                print("Opção inválida, Tente novamente.")
                return

