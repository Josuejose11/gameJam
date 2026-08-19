from utilidades import *
def sql():
    try:
        conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Senac2026',
        )
        
    except Error as e:
        print(f"Erro ao conectar: {e}")

    



    
    if conn is None:
        print("Erro ao conectar com o banco!")
        return False

    cursor = conn.cursor()


    cursor.execute("CREATE DATABASE IF NOT EXISTS Hakaton")
    cursor.execute("USE Hakaton")
    

    # Criação da tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL
        )
    """)

    # Criação da tabela de conversas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_usuario INT NOT NULL,
            mensagem_usuario TEXT NOT NULL,
            resposta_ia TEXT NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()