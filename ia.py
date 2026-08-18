from concurrent.futures import thread

from google import genai
from google.genai import types
import time
import threading        

pensando = False


# def Nenhuma das opções anteriores  
def nenhuma_das_opcoes():
    prompt = input("Fale para a nossa IA o seu problema para que nós possamos te ajudar: ")
    gemini(prompt)

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
    client = genai.Client(api_key="SUA_CHAVE_API")  # Substitua pelo seu token de API do Gemini

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

    return response.text
  
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



