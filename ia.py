from google import genai
from google.genai import types

import warnings

warnings.filterwarnings(
    "ignore",
    message="Direct use of automatic function calling*"
)


def gemini(texto):
    client = genai.Client(api_key="SUA_API_AQUI")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=texto
    )
    return response.text

msg = input("Digite uma mensagem para o gemini: ")
print ("Pensando...")
print(gemini("Me de apenas a resposta simples para: " + msg))