from mysql.connector import connect
from mysql.connector import Error

#Cria conexao com o sql
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
    cursor = conn.cursor()
    sql = "SELECT * FROM usuarios WHERE id_usuario = %s AND senha = %s"
    valores = (id_usuario, senha)
    cursor.execute(sql, valores)
    resultado = cursor.fetchall()  
   
    cursor.close()
    conn.close()
 
    if not resultado:
        print (f"------------")
        print("Senha não encontrada")
        print (f"------------")
        return False

    return True

# cria o login 
def criar_login(nome, email, senha):
    # a lógica para criar o login com os dados fornecidos

    ler_usuarios()

#le os usuarios 
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
    