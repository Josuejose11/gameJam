import utilidades
from google import genai
from google.genai import types
from utilidades import *     
import time
import threading  

# def Nenhuma das opções anteriores  
def nenhuma_das_opcoes(texto = ""):
    print ("---------------")
    prompt = input("Fale para a nossa IA sobre o seu problema para que nós possamos te ajudar\nQual o problema presente na sua empresa: ")
    Ia(texto + prompt)

#def de "Pensando..." 
def carregando():
    global pensando

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
    client = genai.Client(api_key="sua_chave_de_api")  # Substitua pelo seu token de API do Gemini

    config = types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Chat: "+ resposta,
        config=config
    )

    resposta = response.text
    
    return resposta 


def salvar_conversa(id_usuario, mensagem_usuario, resposta_ia):
    conn = criar_conexao()

    if conn is None:
        print("Erro ao conectar com o banco!")
        return False

    cursor = conn.cursor()

    sql = """
        INSERT INTO HistoricoConversas
        (id_usuario_fk, mensagem_usuario, resposta_ia)
        VALUES (%s, %s, %s)
    """

    valores = (id_usuario, mensagem_usuario, resposta_ia)

    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()

    return True

#  def de inicio da conversa c a ia
def Ia(msg):
    while True:
        email = input("Antes de enviar a mensagem, precisamos do seu email: ")
        id_usuario = encontrar_id_usuario(email)
        if id_usuario:
            break
        print("Email não encontrado. Por favor, tente novamente.")

    global pensando

    pensando = True
    thread = threading.Thread(target=carregando)
    thread.start()

    resposta = gemini(msg)

    pensando = False
    thread.join()
    print ("\n\nChat: " + resposta)
    salvar_conversa(id_usuario, msg, resposta)
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

                

    

    

