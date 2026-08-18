import mysql.connector  # Corrigido o import para aceitar mysql.connector.connect
from mysql.connector import Error
import validacoes  # Alterado para importar o módulo e permitir chamadas 'validacoes.funcao'

# Cria conexao com o sql
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database='carrossel'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

# entra no login do docente 
def entrar(id_usuario, senha):
    conn = criar_conexao()
    if not conn:
        return False
        
    cursor = conn.cursor()
    sql = "SELECT * FROM usuarios WHERE id_usuario = %s AND senha = %s"
    valores = (id_usuario, senha)
    cursor.execute(sql, valores)
    resultado = cursor.fetchall()  
   
    cursor.close()
    conn.close()
 
    if not resultado:
        print("------------")
        print("Senha ou usuário não encontrado")
        print("------------")
        return False

    return True

# cria o login 
def criar_login(nome, email, senha):
    conn = criar_conexao() 
    cursor = conn.cursor()

    sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()

# lê os usuários e RETORNA os valores
def ler_usuarios():
    conn = criar_conexao()
    cursor = conn.cursor()

    if conn is None:
        print("Erro ao conectar com o banco!")
        return


    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)

    resultado = cursor.fetchall()

    if not resultado:
        print("======================")
        print("Nenhum aluno cadastrado")
        print("======================")
        cursor.close()
        conn.close()
        return False
    else:
        print("======================")
        print("LISTA DE ALUNOS")
        print("======================")

        for aluno in resultado:
            print(
                f"Id: {aluno[0]} | "
                f"Nome: {aluno[1]} | "
            )

    cursor.close()
    conn.close()
    return True
    
# def de informacoes
def informacoes():
    # Busca os usuários chamando a função correspondente
    id_usuario, senha = ler_usuarios()
    
    # Valida o login usando a função local 'entrar'
    if id_usuario and entrar(id_usuario, senha):
        print("\nLogin bem-sucedido!")
    else:
        print("Falha no login. Tente novamente.")
        return  # Encerra a função caso o login falhe

    print("\nBem-vindo ao programa de sustentabilidade!")
    
    sust = "Sustentabilidade é a capacidade de usar os recursos da Terra com inteligência. O objetivo é atender às necessidades do presente sem acabar com o futuro. O conceito busca um equilíbrio entre cuidar do planeta, fazer a economia crescer e ajudar a sociedade."
    como = "Como podemos contribuir para a sustentabilidade? Podemos economizar energia, reciclar, reduzir o consumo de água, plantar árvores e apoiar empresas que se preocupam com o meio ambiente. Cada pequena ação conta!"
    beneficios = "Os benefícios da sustentabilidade são muitos. Ela ajuda a proteger o meio ambiente, melhora a qualidade de vida das pessoas, promove a economia verde e garante que as futuras gerações possam viver em um planeta saudável."
    economia = "Além de todos os benefícios ambientais, a sustentabilidade também pode trazer vantagens econômicas. Empresas que adotam práticas sustentáveis podem reduzir custos, atrair clientes conscientes e se destacar no mercado."

    while True:
        print("\nEscolha uma opção:")
        print("1. Sustentabilidade")
        print("2. Como contribuir")
        print("3. Benefícios")
        print("4. Economia")
        print("5. Sair")
        
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            print(f"\n{sust}")
        elif escolha == "2":
            print(f"\n{como}")
        elif escolha == "3":
            print(f"\n{beneficios}")
        elif escolha == "4":
            print(f"\n{economia}")
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    informacoes()


if __name__ == "__main__":
    main()
    ...

# def de solucao de problemas
def solucao_problemas():
    print("==================")
    print("Para entendermos sobe o que se trata o problema precisamos saber em qual categoria ele se classifica")
    print("| 1 -  Ambiental \n | 2 -  Econômico")




