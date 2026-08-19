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
        continuar = input("Deseja fazer mais alguma coisa em nosso sistema? \n1 - Sim \n2 - Não \nDigite aqui: ")

        if continuar.strip() == "":
            print("Campo vazio!")
            continue

        elif continuar == "1":
            print("=================\n")
            return

        elif continuar == "2":
            print("Você saiu, obrigado por ultilizar nosso sistema!")
            exit()
        else: 
            print("Valor inválido por favor responda com 1 ou 2.")
        print("=================")

#def validar nome
def validar_nome(nome):
    nome = " ".join(nome.split())

    if nome == "":
        print("Campo vazio!") 
        return False
    if nome.replace(" ", "").isalpha():
        return nome

    return False

#def validar email
def validar_email(Email):
    if Email.strip() == "":
        erro()
        print("Campo vazio!")
        return False

    arroba = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com", "@prof.sc.senac.br" ]

    if not any(a in Email for a in arroba):
        print("Coloque o email corretamente")
        erro()
        return False

    return True

# valida a senha na hora do create 
def validar_senha():
    while True:

        senha = input("Crie a sua senha: ").strip()

        if senha.strip() == "":
            print("Campo vazio!")  
            continue 


        letra = any(caracter.isalpha() for caracter in senha)
        num = any(caracter.isdigit() for caracter in senha)
        carac = any(not caracter.isalnum() for caracter in senha)
 
        if len(senha) > 10 or len(senha) < 1:
            print("Coloque entre 1 e 10 valores")
            continue
           
        if letra and num and carac:
            print("Senha valida")
            return senha
            
            
        else:
            print ("=================")
            if not letra:
                print ("Precisa de letra")
                

            if not num:
                print ("Precisa de numero")
                
                
            if not carac:
                print ("Precisa de caracter especial")
                
                

            print ("Tente de novo")
            print ("============")
            continue

# valida o id do docente que o usuario colocou 
def validar_id():
    
    while True:
        conn = criar_conexao()
        cursor = conn.cursor()
        
        id_usuario = input("Digite seu ID: ").replace(" ", "")

        if id_usuario.strip() == "":
            print("Campo vazio!")
            continue

        if not id_usuario.isdigit():
            print("Apenas números!")
            continue

        sql = "SELECT id_usuario FROM usuarios WHERE id_usuario = %s"

        cursor.execute(sql, (id_usuario,))

        resultado = cursor.fetchone()

        if resultado is None:
            print("ID inválido!")
            continue
        
        cursor.close()
        conn.close()

        return id_usuario








    # a lógica para ler os usuários existentes
    ...