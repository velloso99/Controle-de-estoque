# Importando banco de dados
import sqlite3
import hashlib

# Criando conexão
try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conectar com Banco de Dados!")

# Tabela de Login------------------------------------------------------------
def criar_login(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO login (usuario, senha) values(?,?)"
        cur.execute(query, i)
        
def verificar_usuario(usuario):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM login WHERE usuario=?", (usuario,))
    resultado = cursor.fetchall()
    cursor.close()
    return bool(resultado)    

def atualizar_Login(i):
    with con:
        cur = con.cursor()
        query = "UPDATE login SET usuario=?, senha=? WHERE id=?"
        cur.execute(query, i)  # A variável 'dados' já é uma tupla
        con.commit()

        # Retorna True se a atualização for bem-sucedida
        return cur.rowcount > 0
        
def ver_login():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM login')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista  

# deletar os  Cursos (Delete D) 
def deletar_usuario(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM login WHERE id=? "
        cur.execute(query, i) 

#Tabela de estoque-------------------------------------------------------------
def criar_estoque(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO estoque (fornecedor, produto, quantidade, categoria, preco_custo,valor_total_em_estoque, ean, valor_total_Produto ) values(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
#Ver estoque----------------------------------------------------------------------
def ver_estoque():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM estoque')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista 
# atualizar estoque----------------------------------------------------------------    
def atualizar_estoque(i):
    with con:
        cur = con.cursor()
        query = "UPDATE estoque SET fornecedor=?, produto=?, quantidade=?, categoria=?,  preco_custo=?,valor_total_Produto=? ,valor_total_em_estoque=?, ean=?  WHERE id=?"
        cur.execute(query, i)       
# Deletar alunos(deletar D)----------------------------------------------------
def deletar_estoque(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM estoque WHERE id=?"
        cur.execute(query, i)        
#*******************************************************************************  
#Tabela de fornecedor------------------------------------------------------------- 
def criar_fornecedor(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO fornecedor (cnpj, razao_social, nome_fantasia, vendedor) values(?,?,?,?)"
        cur.execute(query, i)

def Ver_fornecedor():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM fornecedor')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista    
        
#******************************************************************************************
#Criar Categoria----------------------------------------------------------------------------
def criar_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO categoria (nome) VALUES (?)"
        cur.execute(query, i)
        con.commit()     
        
def ver_categoria():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT nome FROM categoria')  # Seleciona apenas os nomes
        linha = cur.fetchall()
        
        # Extrai apenas os nomes das categorias
        lista = [i[0] for i in linha]
    return lista          
        
        