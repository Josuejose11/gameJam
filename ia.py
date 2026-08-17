
from google import genai

client = genai.Client(api_key="Sua_API_KEY_Aqui")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Olá! Responda apenas: Funcionou!"
)

print(response.text)