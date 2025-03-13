# Importando banco de dados
import sqlite3

# Criando conexão
try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conectar com Banco de Dados!")
    
# Criando tabelas do Banco de Dados
#Tabela de Login--------------------------------------
try:
    with con:
        cur = con.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS login(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT,
                senha TEXT
            )""")
        print("Tabela de login criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela de login!")

#Tabela de Estoque----------------------------------------------------------------------------
try:
    with con:
        cur = con.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS estoque(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fornecedor TEXT,
                produto TEXT,
                quantidade TEXT,
                categoria TEXT,
                preco_custo DECIMAL,
                valor_total_Produto DECIMAL,
                valor_total_em_estoque DECIMAL,
                ean NUMERIC,
                
                FOREIGN KEY(fornecedor) REFERENCES fornecedor(nome_fantasia) ON UPDATE CASCADE ON DELETE CASCADE
                FOREIGN KEY(categoria) REFERENCES categoria(nome) ON UPDATE CASCADE ON DELETE CASCADE
                )""")
        print("Tabela de estoque criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela de estoque !")

#Tabela de fornecedor
try:
    with con:
        cur = con.cursor() 
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS fornecedor(                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cnpj NUMERIC,
                razao_social TEXT,
                nome_fantasia TEXT,
                vendedor TEXT
            )""")
        print("Tabela de fornecedor criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar fornecedor de caixa!")  
                    
#Tabela de categoria
try:
    with con:
        cur = con.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS categoria(                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )""")
        
        print("Tabela 'categoria' criada com sucesso!")
except sqlite3.Error as e:
    print(f"Erro ao criar tabela: {e}") 










