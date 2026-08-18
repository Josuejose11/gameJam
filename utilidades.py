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

#def fazer denovo
def denovo():
    while True:
        print("=================")
        continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")

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

    if conn is None:
        print("Erro ao conectar com o banco!")
        return


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


    sql = "SELECT * FROM Usuarios"
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

# def de solucao de problemas
def solucao_problemas():
    while True:
        print("==================")
        print("Para entendermos sobre o que se trata o problema precisamos saber em qual categoria ele se classifica")
        print(" | 0 - Sair \n | 1 -  Ambiental \n | 2 -  Econômico \n | 3 - Bioeconomia (Ambiental e econômico)")
        escolha = input("| Escreva aqui: ").strip()

        match escolha:
            case "0":
                print ("Você saiu")               
                exit()
            case "1":
                ambiental()
            case "2":
                economico()
            case "3":
                bioeconomia()
            case _:
                print("Opção inválida, Tente novamente.")
                continue

        denovo() 

# def para a funcao ambiental dentro da solucao de problemas
def ambiental():
    print("Em quais dessas classificações o seu problema se encaixa?")
    print(" | 1 - Poluição \n | 2 - Desmatamento \n | 3 - Mudanças climáticas \n | 4 - Perda de biodiversidade \n | 5 - Esgotamento de recursos naturais\n | 6 - Nenhuma das opções enteriores")
    escolha = input("Escreva aqui: ")

    match escolha:
        case "1":
            print("Poluição é a introdução de substâncias ou energia no meio ambiente que causam efeitos adversos. Isso pode incluir poluição do ar, da água e do solo, afetando a saúde humana e os ecossistemas.")
        case "2":
            print("Desmatamento é a remoção de árvores e vegetação de uma área, geralmente para fins agrícolas ou urbanos, resultando em perda de habitat e biodiversidade.")
        case "3":
            print("Mudanças climáticas são alterações nos padrões climáticos globais, causadas principalmente pela atividade humana, afetando ecossistemas e sociedades.")
        case "4":
            print("Perda de biodiversidade é a diminuição da variedade de espécies vivas em um ecossistema, frequentemente causada por atividades humanas.")
        case "5":
            print("Esgotamento de recursos naturais é a degradação ou exaustão de recursos renováveis ou não renováveis, como água, minerais e florestas.")
        case "6":
            print("Nenhuma das opções anteriores.")
        case _:
            print("Opção inválida, Tente novamente.")

# def para a funcao economico dentro da solucao de problemas
def economico():
    print("Em quais dessas classificações o seu problema se encaixa?")
    print(" | 1 - Crise econômica \n | 2 - Desemprego \n | 3 - Inflação \n | 4 - Dívida pública \n | 5 - Instabilidade econômica\n | 6 - Nenhuma das opções enteriores")
    escolha = input("Escreva aqui: ")
    match escolha:
        case "1":
            ...
        case "2":
            ...
        case "3":
            ...
        case "4":
            ...
        case "5":
            ...
        case "6":
            ...
        case _:
            print("Opção inválida, Tente novamente.")

# def para a funcao ambiental e economico dentro da solucao de problemas
def bioeconomia():
    print("Em quais dessas classificações o seu problema se encaixa?")
    print (" | 1 - Desperdício de matéria-prima orgânica\n |  2 - Uso excessivo de recursos naturais\n | 3 - Alto custo de matérias-primas sustentáveis\n | 4 - Falta de tecnologia para reaproveitamento \n | 5 - Nenhuma das opções enteriores")
    escolha  = input ("Escreva aqui: ")
    match escolha:
        case "1":
            print ("Para o problema do desperdicio de matéria-prima orgânica temos algumas classificações, selecione a que mais se encaixa com o seu problema")
            print (" | 1 - Excesso de resíduos orgânicos \n | 2 - Falta de reaproveitamento\n | 3 - Perda de matéria-prima durante a produção\n | 4 - Nenhuma das opções anteriores")
            escolha  = input (" | Escreva aqui: ")
            ...

        case "2":
            print ("Para o problema do uso excessivo de recursos naturais temos algumas classificações, selecione a que mais se encaixa com o seu problema")
            print (" | 1 - Consumo excessivo de água \n | 2 - Consumo excessivo de madeira \n | 3 - Uso excessivo de recursos agrícolas\n | 4 - Uso excessivo de recursos agrícolas\n | 5 - Nenhuma das opções anteriores")
            escolha  = input (" | Escreva aqui: ")
            ...
                
        case "3":
            ... 
        case "4":
            ... 
        case "5":
            ... 
        case "6":
            ...
        