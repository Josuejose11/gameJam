import mysql.connector
from mysql.connector import Error
from utilidades import criar_conexao

#bloco de prinst para erro
def erro():
    print("---------------------------")
    print("*Ocorreu um erro tente novamente*")
    print("---------------------------")

#def fazer denovo
def denovo():
    while True:
        print("=================")

        continuar = input(
            "Deseja fazer mais alguma coisa em nosso sistema?\n"
            "1 - Sim\n"
            "2 - Não\n"
            "Digite aqui: "
        ).strip()

        if continuar == "":
            print("Campo vazio!")
            continue

        if continuar == "1":
            print("=================\n")
            return

        if continuar == "2":
            print("Você saiu, obrigado por utilizar nosso sistema!")
            exit()

        print("Valor inválido. Por favor, responda com 1 ou 2.")

#def validar nome
def validar_nome(nome):
    # Remove espaços extras
    nome = " ".join(nome.strip().split())

    if nome == "":
        print("Campo vazio!")
        return False

    # Remove os espaços para verificar somente as letras
    nome_sem_espacos = nome.replace(" ", "")

    if not nome_sem_espacos.isalpha():
        print("O nome deve conter apenas letras.")
        return False

    return nome

#def validar email
def validar_email(email):

    email = email.strip().lower()

    if email == "":
        erro()
        print("Campo vazio!")
        return False

    arroba = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com" ]

    if not any(a in Email for a in arroba):
        print("Coloque o email corretamente")
        erro()
        print("Email inválido!")
        return False

    usuario, dominio = email.split("@")

    # Verifica se existe algo antes do @
    if usuario == "":
        erro()
        print("Email inválido!")
        return False

    # Não permite espaços
    if " " in email:
        erro()
        print("O email não pode conter espaços!")
        return False

    # Domínios permitidos
    dominios_permitidos = [
        "gmail.com",
        "hotmail.com",
        "outlook.com",
        "yahoo.com",
        "prof.sc.senac.br"
    ]

    # Verifica o domínio
    if dominio not in dominios_permitidos:
        erro()
        print("Domínio de email não permitido!")
        print("Use Gmail, Hotmail, Outlook, Yahoo ou Senac.")
        return False

    return email


# valida a senha na hora do create 
def validar_senha():

    while True:

        senha = input("Crie a sua senha: ").strip()

        if senha == "":
            print("Campo vazio!")
            continue

        # Limite da senha
        if len(senha) < 6 or len(senha) > 10:
            print("A senha deve ter entre 6 e 10 caracteres.")
            continue

        # Precisa ter pelo menos uma letra
        letra = any(caracter.isalpha() for caracter in senha)

        # Precisa ter pelo menos um número
        numero = any(caracter.isdigit() for caracter in senha)

        # Precisa ter pelo menos um caractere especial
        especial = any(
            not caracter.isalnum()
            for caracter in senha
        )

        if not letra:
            print("A senha precisa ter pelo menos uma letra.")

        if not numero:
            print("A senha precisa ter pelo menos um número.")

        if not especial:
            print(
                "A senha precisa ter pelo menos "
                "um caractere especial."
            )

        if letra and numero and especial:
            print("Senha válida!")
            return senha

        print("=================")
        print("Tente novamente.")
        print("=================")


# valida o id do docente que o usuario colocou 
def validar_id():

    while True:

        id_usuario = input("Digite seu ID: ").strip()

        if id_usuario == "":
            print("Campo vazio!")
            continue

        if not id_usuario.isdigit():
            print("Apenas números!")
            continue

        conn = criar_conexao()

        if conn is None:
            print("Erro ao conectar com o banco de dados!")
            return False

        cursor = conn.cursor()

        try:

            sql = """
                SELECT id_usuario
                FROM usuarios
                WHERE id_usuario = %s
            """

            cursor.execute(sql, (id_usuario,))
            resultado = cursor.fetchone()

            if resultado is None:
                print("ID inválido!")
                continue

            return id_usuario

        except Error as e:

            print(f"Erro ao consultar o ID: {e}")
            return False

        finally:

            cursor.close()
            conn.close()








    # a lógica para ler os usuários existentes
    ...