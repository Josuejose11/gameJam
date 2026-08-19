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
        CREATE TABLE IF NOT EXISTS Usuarios (
            id_usuario INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100),
            email VARCHAR(100),
            senha VARCHAR(100)
        );
    """)

    # Criação da tabela de conversas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS HistoricoConversas (
            id_usuario_fk INT,
            horario DATETIME DEFAULT CURRENT_TIMESTAMP,
            mensagem_usuario TEXT,
            resposta_ia TEXT,
            FOREIGN KEY (id_usuario_fk) REFERENCES Usuarios(id_usuario)
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()
    