Hakaton — Sistema de Suporte em Sustentabilidade

Sistema de suporte em linha de comando (CLI) desenvolvido em Python, criado durante um hackathon/game jam. A proposta é ajudar empresas a identificar desafios de sustentabilidade e receber sugestões de soluções sustentáveis, com apoio de uma IA (Google Gemini) para gerar recomendações personalizadas.

## Funcionalidades

- **Cadastro e login de empresas**, com validação de nome, e-mail e senha (regras de domínio de e-mail e força de senha).
- **Conteúdo informativo** sobre sustentabilidade (econômica, social e bioeconômica).
- **Diagnóstico guiado de problemas**, através de um menu em árvore que classifica o problema da empresa em:
  - Ambiental (poluição, desmatamento, mudanças climáticas, perda de biodiversidade, esgotamento de recursos naturais);
  - Econômico;
  - Bioeconômico (ambiental + econômico).
- **Chat com IA (Google Gemini)** para gerar sugestões de soluções sustentáveis com base no problema identificado.
- **Histórico de conversas** salvo em banco de dados MySQL, vinculado ao usuário.
- Feedback do usuário sobre a utilidade da resposta da IA.

## Tecnologias

- **Python 3**
- **MySQL** (via `mysql-connector-python`)
- **Google Gemini API** (via `google-genai`)
- `pwinput` (entrada de senha mascarada no terminal)

## Estrutura do projeto

```
gameJam-QA/
├── main.py          # Ponto de entrada: login, cadastro e inicialização do banco
├── menu.py          # Menu principal pós-login
├── utilidades.py     # Conexão com banco, CRUD de usuários, integração com a IA
├── validacoes.py     # Validações de nome, e-mail, senha e ID
├── prompts.py        # Prompts pré-definidos usados para consultar a IA
├── sql.py            # Criação inicial do banco de dados e tabelas
└── hakaton.sql        # Script SQL para criação manual do banco (Usuarios, HistoricoConversas)
```

## Pré-requisitos

- Python 3.10+ instalado (o projeto usa `match/case`).
- Um servidor **MySQL** rodando localmente (ou acessível pela rede).
- Uma chave de API do **Google Gemini**.

## Instalação

1. Clone o repositório:
   ```bash
   git clone -b QA https://github.com/Josuejose11/gameJam.git
   cd gameJam
   ```

2. (Recomendado) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install mysql-connector-python pwinput google-genai
   ```

## Configuração

O projeto se conecta a um banco MySQL local e à API do Gemini. Atualmente as credenciais estão fixas diretamente no código (`sql.py`, `utilidades.py` e a chave da API em `utilidades.py`, na função `gemini`).

**Antes de rodar, ajuste:**

1. **Banco de dados** — edite os parâmetros de conexão (`host`, `user`, `password`) em `sql.py` e `utilidades.py` para os do seu ambiente MySQL. O banco `Hakaton` e as tabelas (`Usuarios`, `HistoricoConversas`) são criados automaticamente ao rodar `main.py`, ou você pode executar `hakaton.sql` manualmente.

2. **Chave da API do Gemini** — substitua o valor de `api_key` na função `gemini()` (em `utilidades.py`) pela sua própria chave.

> **Recomendação de segurança:** por enquanto o usuário/senha do banco e a chave de API ficam hardcoded no código-fonte. Para uso além de testes locais, mova esses valores para variáveis de ambiente (ex: com `python-dotenv`) e evite versioná-los no Git.

##  Como executar

```bash
python main.py
```

Ao iniciar, o sistema:
1. Garante que o banco de dados e as tabelas existam;
2. Exibe o menu inicial para **entrar** com uma conta existente ou **criar login** para uma nova empresa;
3. Após o login, abre o menu principal com acesso a conteúdo sobre sustentabilidade e ao diagnóstico guiado de problemas com sugestões geradas por IA.

##  Fluxo de uso

1. Crie um cadastro de empresa (nome, e-mail e senha).
2. Faça login com o ID da empresa e a senha cadastrada.
3. No menu principal, escolha entre ver informações sobre sustentabilidade ou iniciar a solução de problemas.
4. Navegue pelas classificações do seu problema (Ambiental / Econômico / Bioeconômico) até a categoria mais específica.
5. Receba uma sugestão gerada pela IA e avalie se a resposta foi útil.

## Sobre o projeto

Projeto desenvolvido durante uma game jam/hackathon com foco em soluções sustentáveis para empresas.

## Licença

MIT 
