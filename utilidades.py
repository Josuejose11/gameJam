import mysql.connector
from mysql.connector import Error
from prompts import *


# Cria conexao com o sql
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database='Hakaton'
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

    if conn is None:
        print("Erro ao conectar com o banco!")
        return False

    cursor = conn.cursor()

    try:
        sql = """
            SELECT id_usuario
            FROM usuarios
            WHERE id_usuario = %s AND senha = %s
        """

        valores = (id_usuario, senha)

        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

    except Error as e:
        print(f"Erro ao realizar login: {e}")
        return False

    finally:
        cursor.close()
        conn.close()

    if resultado:
        return True

    print("------------")
    print("Senha ou usuário não encontrado")
    print("------------")

    return False


# cria o login 
def criar_login(nome, email, senha):
    conn = criar_conexao()

    if conn is None:
        print("Erro ao conectar com o banco!")
        return False

    cursor = conn.cursor()

    sql = "INSERT INTO Usuarios (nome, email, senha) VALUES (%s, %s, %s)"
    valores = (nome, email, senha)

    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()

    return True


#encontrar id usuario
def encontrar_id_usuario(email):
    conn = criar_conexao()

    if conn is None:
        return None

    cursor = conn.cursor()

    try:
        sql = "SELECT id_usuario FROM usuarios WHERE email = %s"
        cursor.execute(sql, (email,))

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]

        print("Email não encontrado no banco de dados.")
        return None

    except Error as e:
        print(f"Erro ao procurar usuário: {e}")
        return None

    finally:
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
        print("Nenhuma empresa cadastrada")
        print("======================")
        cursor.close()
        conn.close()
        return False
    else:
        print("==============================")
        print("LISTA DE EMPRESAS CADASTRADAS")
        print("==============================")

        for empresa in resultado:
            print(
                f"Id: {empresa[0]} | "
                f"Nome: {empresa[1]} | "
            )

    cursor.close()
    conn.close()
    return True
    
# def de informacoes
def informacoes():
    Economico = "Sustentabilidade econômica é a capacidade de uma economia de crescer e se desenvolver de forma equilibrada, garantindo a geração de riqueza, emprego e renda para a sociedade, sem comprometer os recursos naturais e o bem-estar das gerações futuras."
    Social = "Sustentabilidade social é a capacidade de uma sociedade de manter e melhorar o bem-estar de seus membros, garantindo igualdade, justiça e qualidade de vida para todos." 
    Bioeconomico = "Podemos definir bioeconomia como um modelo econômico fundamentado no uso sustentável de recursos biológicos renováveis "

    while True:
        print("\nEscolha uma opção:")
        print("0 - Sair")
        print("1 - Economico")
        print("2 - Social")
        print("3 - Bioeconomico")
        
        escolha = input("Digite a opção desejada: ")

        if escolha == "1":
            print(f"\n{Economico}")
        elif escolha == "2":
            print(f"\n{Social}")
        elif escolha == "3":
            print(f"\n{Bioeconomico}")
        elif escolha == "0":
            print("Saindo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

        break

    denovo()

# def de solucao de problemas
def solucao_problemas():
    while True:
        print()
        print("Para entendermos sobre o que se trata o problema precisamos saber em qual categoria ele se classifica")
        print(" | 0 - Sair \n | 1 -  Ambiental \n | 2 -  Econômico \n | 3 - Bioeconomia (Ambiental e econômico)")
        escolha = input(" | Escreva aqui: ").strip()
        print ("=================")

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
    from ia import Ia, nenhuma_das_opcoes
    while True:
        print("Em quais dessas classificações o seu problema se encaixa?")
        print(" | 1 - Poluição \n | 2 - Desmatamento \n | 3 - Mudanças climáticas \n | 4 - Perda de biodiversidade \n | 5 - Esgotamento de recursos naturais\n | 6 - Nenhuma das opções enteriores")
        escolha = input("Escreva aqui: ")

        match escolha:
            case "1":
                print ("Sobre poluição podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema.")
                print(" | 1 - Poluição do ar \n | 2 - Poluição da água \n | 3 - Poluição do solo \n | 4 - Poluição sonora \n | 5 - Poluição luminosa \n | 6 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (Bio1_1)
                    case "2":
                        Ia (Bio1_2)
                    case "3":
                        Ia (Bio1_3)
                    case "4":
                        Ia (Bio1_4)
                    case "5":
                        Ia (Bio1_5)
                    case "6":
                        nenhuma_das_opcoes(Bio1)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue

            case "2":
                print("Sobre desmatamento podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema.")
                print(" | 1 - Desmatamento em larga escala \n | 2 - Desmatamento para agricultura \n | 3 - Desmatamento para urbanização \n | 4 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (Bio2_1)
                    case "2":
                        Ia (Bio2_2)
                    case "3":
                        Ia (Bio2_3)
                    case "4":
                        nenhuma_das_opcoes(Bio2)
                    case _:
                        print("Opção inválida, Tente novamente.")   
                        continue

            case "3":
                print("Sobre mudanças climáticas podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema.")
                print(" | 1 - Aquecimento global \n | 2 - Alterações nos padrões de chuva \n | 3 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case"1":
                        Ia (Bio3_1)
                    case "2":
                        Ia (Bio3_2)
                    case"3":
                        nenhuma_das_opcoes(BioE3)
                    case _:
                        print("Opção inválida, Tente novamente.")   
                        continue    

            case "4":
                print("Sobre perda de biodiversidade podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema.")
                print(" | 1 - Perda de habitat \n | 2 - Extinção de espécies \n | 3 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (Bio4_1)
                    case "2":
                        Ia (Bio4_2)
                    case "3":
                        nenhuma_das_opcoes(Bio4)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue

            case "5":
                print("Sobre esgotamento de recursos naturais podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema.")
                print(" | 1 - Esgotamento de água \n | 2 - Esgotamento de minerais \n | 3 - Esgotamento de florestas \n | 4 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (Bio5_1)        
                    case "2":
                        Ia (Bio5_2)
                    case "3":
                        Ia (Bio5_3)
                    case "4":
                        nenhuma_das_opcoes(Bio5)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue

            case "6":
                nenhuma_das_opcoes()

            case _:
                print("Opção inválida, Tente novamente.")
                continue

# def para a funcao economico dentro da solucao de problemas
def economico():
    from ia import Ia, nenhuma_das_opcoes
    while True:
        print("Em quais dessas classificações o seu problema se encaixa?")
        print(" | 1 - Crise econômica \n | 2 - Desemprego \n | 3 - Inflação \n | 4 - Dívida pública \n | 5 - Instabilidade econômica\n | 6 - Nenhuma das opções enteriores")
        escolha = input("Escreva aqui: ")

        match escolha:
            case "1":
                print("----------------------------------")
                print(" | 1 - Aumento dos custos de produção \n | 2 - Queda na produção \n | 3 - Perda de matéria-prima durante a produção\n | 4 - Individamento Empresarial \n | 5 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (E1_1)
                    case "2":
                        Ia (E1_2)
                    case "3":
                        Ia (E1_3)
                    case "4":
                        Ia (E1_4)
                    case "5":
                        nenhuma_das_opcoes(E1)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue

            case "2":
                print ("Sobre desemprego podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema.")
                print("| 1 - Aumento do custo de mão de obra \n | 2 - Redução da demanda por trabalhadores \n | 3 - Substituição de trabalhadores por tecnologia \n | 4 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (E2_1)
                    case "2":
                        Ia (E2_2)
                    case "3":
                        Ia (E2_3)
                    case "4":
                        nenhuma_das_opcoes(E2)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue 

            case "3":
                print("Sobre inflação podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema.")
                print("| 1 - Aumento dos preços de bens e serviços \n | 2 - Aumento dos custos de produção \n | 3 - Perda de poder de compra da moeda \n | 4 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (E3_1)
                    case "2":
                        Ia (E3_2)
                    case "3":
                        Ia (E3_3)
                    case "4":
                        nenhuma_das_opcoes(E3)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue

            case "4":
                print("Sobre dívida pública podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema.")
                print("| 1 - Aumento do endividamento governamental \n | 2 - Redução da receita fiscal \n | 3 - Aumento dos juros da dívida \n | 4 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (E4_1)
                    case "2":  
                        Ia (E4_2)
                    case "3":
                        Ia (E4_3)
                    case "4":
                        nenhuma_das_opcoes(E4)
                    case _: 
                        print("Opção inválida, Tente novamente.")
                        continue

            case "5":
                print("Sobre instabilidade econômica podemos dizer que existem algumas classificações, escolha qual se encaixa melhor com o seu problema .")
                print("| 1 - Flutuações significativas na economia \n | 2 - Impactos negativos no crescimento econômico \n | 3 - Efeitos sobre o emprego \n | 4 - Nenhuma das opções anteriores")
                escolha = input("Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (E5_1)
                    case "2":  
                        Ia (E5_2)
                    case "3":
                        Ia (E5_3)
                    case "4":
                        nenhuma_das_opcoes(E5)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue

            case "6":
                nenhuma_das_opcoes()

            case _:
                print("Opção inválida, Tente novamente.")
                continue    

# def para a funcao ambiental e economico dentro da solucao de problemas
def bioeconomia():
    from ia import Ia, nenhuma_das_opcoes
    while True:
        print("Em quais dessas classificações o seu problema se encaixa?")
        print (" | 1 - Desperdício de matéria-prima orgânica\n |  2 - Uso excessivo de recursos naturais\n | 3 - Alto custo de matérias-primas sustentáveis\n | 4 - Falta de tecnologia para reaproveitamento \n | 5 - Nenhuma das opções enteriores")
        escolha  = input ("Escreva aqui: ")

        match escolha:
            case "1":
                print ("Para o problema do desperdicio de matéria-prima orgânica temos algumas classificações, selecione a que mais se encaixa com o seu problema")
                print (" | 1 - Excesso de resíduos orgânicos \n | 2 - Falta de reaproveitamento\n | 3 - Perda de matéria-prima durante a produção\n | 4 - Nenhuma das opções anteriores")
                escolha  = input (" | Escreva aqui: ")

                match escolha:
                    case "1":
                        Ia (BioE1_1)
                    case "2":
                        Ia (BioE1_2)
                    case "3":
                        Ia (BioE1_3)
                    case "4":
                        nenhuma_das_opcoes(BioE1)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue
                    
            case "2":
                print ("Para o problema do uso excessivo de recursos naturais temos algumas classificações, selecione a que mais se encaixa com o seu problema")
                print (" | 1 - Consumo excessivo de água \n | 2 - Consumo excessivo de madeira \n | 3 - Uso excessivo de recursos agrícolas\n | 4 - Nenhuma das opções anteriores")
                escolha  = input (" | Escreva aqui: ")
                match escolha:
                    case "1":
                        Ia (BioE2_1)
                    case "2":
                        Ia (BioE2_2)
                    case "3":
                        Ia (BioE2_3)
                    case "4":
                        nenhuma_das_opcoes(BioE2)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue
                    
            case "3":
                print ("Para o problema do alto custo de matérias-primas sustentáveis temos algumas classificações, selecione a que mais se encaixa com o seu problema")
                print (" | 1 - Fornecedores sustentáveis mais caros \n | 2 - Baixa disponibilidade\n | 3 - Tecnologia de produção mais cara\n | 4 - Nenhuma das opções anteriores")
                escolha  = input (" | Escreva aqui: ")
                match escolha:
                    case "1":
                        Ia (BioE3_1)
                    case "2":
                        Ia (BioE3_2)
                    case "3":
                        Ia (BioE3_3)
                    case "4":
                        nenhuma_das_opcoes(BioE3)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue

            case "4":
                print ("Para o problema da falta de tecnologia para reaproveitamento temos algumas classificações, selecione a que mais se encaixa com o seu problema")
                print (" | 1 - Falta de equipamentos adequados \n | 2 - Alto custo da tecnologia\n | 3 - Processos antigos ou ineficientes\n | 4 - Nenhuma das opções anteriores")
                escolha  = input (" | Escreva aqui: ")
                match escolha:
                    case "1":
                        Ia (BioE4_1)
                    case "2":
                        Ia (BioE4_2)
                    case "3":
                        Ia (BioE4_3)
                    case "4":
                        nenhuma_das_opcoes(BioE4)
                    case _:
                        print("Opção inválida, Tente novamente.")
                        continue

            case "5":
                nenhuma_das_opcoes() 
    
