from google import genai
from google.genai import types
import time
import threading

#def de "Pensando..." 
def carregando():
    while pensando:
        print("\rPensando   ", end="", flush=True)
        time.sleep(0.5)

        print("\rPensando.  ", end="", flush=True)
        time.sleep(0.5)

        print("\rPensando.. ", end="", flush=True)
        time.sleep(0.5)

        print("\rPensando...", end="", flush=True)
        time.sleep(0.5)

# Def da conexao e cvc c o gemini
def gemini(texto):
    client = genai.Client(api_key="sua_chave_aqui")

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



pensando = True

msg = input("Digite uma mensagem para o Gemini: ")

thread = threading.Thread(target=carregando)
thread.start()

resposta = gemini("Me dê apenas uma resposta simples para: " + msg)

pensando = False
thread.join()

