from mold import*


#Criando a janela
root = tk.Tk()
root.title("Controle de Estoque")
root.geometry("500x300")
root.configure(background=co0)
root.resizable(width=False, height=False)
root.overrideredirect(1)
largura_root = 500
altura_root = 300
#obter tamanho da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

Style = Style(root)
Style.theme_use("clam")
Style.configure("green.Horizontal.TProgressbar", 
                foreground="green", 
                background="green")

#------------------------------------------------------------------------
frame_login = Frame(root, width=500, height=300, bg=co0)
frame_login.grid(row=0 , column=0, sticky=NSEW)
#-----------------------------------------------------------------------
def abrir_novo_usuario():
    for widget in frame_login.winfo_children():
        widget.destroy()
    novo_usuario()

#------------------------------------------------------------------------
def login():
    global root
    # Verificando login e abrir novo arquivo
    def verificar_login():
        
        global usuario, senha 
        
        usuario = e_user.get()
        senha = e_senha.get()
        
        con = sqlite3.connect('database.db')
        cursor = con.cursor()
        cursor.execute("SELECT*FROM login WHERE usuario=? AND senha=?", (usuario, senha))
        resultado = cursor.fetchall()
        if resultado:
            for i in range(101):  # De 0 a 100
                barra['value'] = i  # Atualiza a barra de progresso
                porcentagem_label.config(text=f"{i}%")  # Atualiza o texto da porcentagem
                root.update_idletasks()  # Atualiza a interface
                root.after(5)  # Tempo de espera (20ms)
                
            painel_geral()
            
        else:
            messagebox.showerror("Erro", "Usuario ou senha incorretos!")
        cursor.close()
        
    lbl_status = Label(frame_login, text="", font=('Ivy 15 bold'), bg=co0, fg=co1)
    lbl_status.place(x=325, y=220)

    l_titulo = Label(frame_login, text="Faça seu login", font=('Ivy 20 bold'), bg=co0, fg=co1)
    l_titulo.place(x=240, y=15, anchor=CENTER)

    l_user = Label(frame_login, text="Usuario", font=('Ivy 15 bold'), bg=co0, fg=co1)
    l_user.place(x=240, y=60, anchor=CENTER)
    e_user= Entry(frame_login, width=25, justify=LEFT, font=('Ivy 15 bold'),  relief='solid')
    e_user.place(x=250, y=100, anchor=CENTER)

    l_senha =Label(frame_login, text="Senha", font=('Ivy 15 bold'), bg=co0, fg=co1)
    l_senha.place(x=240, y=140, anchor=CENTER)
    e_senha= Entry(frame_login, width=25, justify=LEFT, font=('Ivy 15 bold'),show="*",  relief='solid')
    e_senha.place(x=250, y=180, anchor=CENTER)

    bt_enter = Button(frame_login, command=verificar_login, text="Enter", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    bt_enter.place(x=45, y=225)

    bt_n_usuario = Button(frame_login, command=abrir_novo_usuario, text="Novo Usuario", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    bt_n_usuario.place(x=110, y=225)
    
    bt_esqueceu = Button(frame_login, command=esqueceu_senha , text="Esqueceu a Senha", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    bt_esqueceu.place(x=240, y=225)

    bt_n_fechar = Button(frame_login, command=root.destroy , text="Fechar", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    bt_n_fechar.place(x=410, y=225)
    
    barra = Progressbar(frame_login, length=250, mode="determinate",style="green.Horizontal.TProgressbar" )
    barra.place(x=170, y=275)
    porcentagem_label =Label(frame_login, text="0%", font=("Arial", 12) )
    porcentagem_label.place(x=120, y=275)

def novo_usuario():
    
    frame_n_senha = Frame(root, width=500, height=300, bg=co0)
    frame_n_senha.grid(row=0, column=0, sticky=NSEW)
    
    def cadastrar_usuario():
        
        usuario = e_user.get().strip()
        senha = e_senha.get().strip()
    
        # Verifica se os campos estão preenchidos
        if not usuario or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        # Verifica se o usuário já existe no banco
        if verificar_usuario(usuario):
            messagebox.showerror("Erro", "Usuário já cadastrado!")
            return
        for i in range(101):  # De 0 a 100
            barra['value'] = i  # Atualiza a barra de progresso
            porcentagem_label.config(text=f"{i}%")  # Atualiza o texto da porcentagem
            root.update_idletasks()  # Atualiza a interface
            root.after(5)  # Tempo de espera (20ms)
            
        root.destroy()
        #subprocess.run(["python", "login.py"])
        # Criar login no banco de dados
        criar_login((usuario, senha))  # Passando como tupla

        # Limpa os campos após o cadastro
        e_user.delete(0, END)
        e_senha.delete(0, END)
        
        
    barra = ttk.Progressbar(frame_n_senha, length=250, mode="determinate",style="green.Horizontal.TProgressbar")
    barra.place(x=170, y=275)
    porcentagem_label = tk.Label(frame_n_senha, text="0%")
    porcentagem_label.place(x=120, y=275)
    
    l_titulo = Label(frame_n_senha, text="Cadastrar um novo usuario", font=('Ivy 20 bold'), bg=co0, fg=co1)
    l_titulo.place(x=230, y=15, anchor=CENTER)
    
    l_user = Label(frame_n_senha, text="Usuario", font=('Ivy 15 bold'), bg=co0, fg=co1)
    l_user.place(x=240, y=60, anchor=CENTER)
    e_user= Entry(frame_n_senha, width=25, justify=LEFT, font=('Ivy 15 bold'),  relief='solid')
    e_user.place(x=250, y=100, anchor=CENTER)

    l_senha =Label(frame_n_senha, text="Senha", font=('Ivy 15 bold'), bg=co0, fg=co1)
    l_senha.place(x=240, y=140, anchor=CENTER)
    e_senha= Entry(frame_n_senha, width=25, justify=LEFT, font=('Ivy 15 bold'),show="*",  relief='solid')
    e_senha.place(x=250, y=180, anchor=CENTER)

    bt_enter = Button(frame_n_senha, command=cadastrar_usuario, text="Enter", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    bt_enter.place(x=105, y=225)
    
    bt_fechar = Button(frame_n_senha, command=root.destroy, text="Atualizar", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    bt_fechar.place(x=200, y=225)
        
def esqueceu_senha():
    
    #Criar uma nova janela
    root1 = Toplevel(root) 
    root1.title("Atulizar Senha")
    root1.geometry("400x400")
    #root.overrideredirect(1)      
    largura_root1 = 400
    altura_root1 = 400
    #obter tamanho da tela
    largura_tela = root1.winfo_screenwidth()
    altura_tela = root1.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root1 )//2
    pos_y = (altura_tela - altura_root1)//2
    # Definir geometria da janela (LxA+X+Y)
    root1.geometry(f"{largura_root}x{altura_root1}+{pos_x}+{pos_y}")   
    
    frame_Login = Frame(root1, width=250, height=300, bg=co0)
    frame_Login.grid(row=0, column=2,padx=0, pady=30 ,sticky=W)

    frame_tabela = Frame(root1, width=250, height=310, bg=co0 )
    frame_tabela.grid(row=0, column=1, sticky=E)
    
    def update_login():
    
        try:
            tree_itens = tree_login.focus()
            tree_dicionario = tree_login.item(tree_itens)
            tree_lista = tree_dicionario['values']
        
            valor_id = tree_lista[0]
        
            e_user.delete(0, END)
            e_senha.delete(0, END)

            e_user.insert(0, tree_lista[1])
            e_senha.insert(0, tree_lista[2])
        
            def update():
            
                user = e_user.get().strip()
                senha = e_senha.get().strip()
            
                lista =[ user, senha, valor_id]
                
                #verificando caso algum campo esteja vazio
                for i in lista:
                    if i == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos!')  
                        return
                atualizar_Login(lista)
                # Mostrando a mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados Atualizados com sucesso!' )    

                # Limpa os campos
                e_user.delete(0, END)
                e_senha.delete(0, END)

                # Chama a função que exibe os logins atualizados (se existir)
                mostrar_login()
                botao_update.destroy()
                
            botao_update = Button(frame_Login, command= update,  anchor=CENTER,text='Salvar e Atualizar'.upper(), width=18, overrelief=RIDGE, font=('Ivy 10'), bg=co3, fg=co1)
            botao_update.place(x=45, y=270) 
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos login na tabela')
    
    def del_usuario():
        try:
            tree_itens = tree_login.focus()
            tree_dicionario = tree_login.item(tree_itens)
            tree_lista = tree_dicionario['values']
            
            valor_id = tree_lista[0]
            
            # deletar dados no Banco de Dados
            deletar_usuario([valor_id])
            
            #Mostrando a menssagem de sucesso
            messagebox.showinfo('Sucesso', 'Usuario e senha deletado com sucesso!')
            
            #mostrando os valores na tabela
            mostrar_login()
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos usuarios na tabela')
            
    l_titulo = Label(root1, text="Atualizar Usuario e Senha", font=('Ivy 20 bold'), bg=co0, fg=co1)
    l_titulo.place(x=201, y=15, anchor=CENTER)
    
    # TRabalhando no frame logo

    l_user = Label(frame_Login, text="Usuario", font=('Ivy 15 bold'), bg=co0, fg=co1)
    l_user.place(x=130, y=15, anchor=CENTER)
    e_user= Entry(frame_Login, width=15, justify=LEFT, font=('Ivy 15 bold'),  relief='solid')
    e_user.place(x=130, y=50, anchor=CENTER)

    l_senha = Label(frame_Login, text="Senha", font=('Ivy 15 bold'), bg=co0, fg=co1)
    l_senha.place(x=130, y=85, anchor=CENTER)
    e_senha= Entry(frame_Login, width=15, justify=LEFT, font=('Ivy 15 bold'),show="*",  relief='solid')
    e_senha.place(x=130, y=120, anchor=CENTER)


    bt_enter = Button(frame_Login, command=update_login, text="Atualizar", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    bt_enter.place(x=85, y=145)

    #bt_voltar = Button(frame_Login, command=voltar_login, text="Voltar", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    #bt_voltar.place(x=95, y=190)

    bt_excluir = Button(frame_Login, command=del_usuario, text="Deletar", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
    bt_excluir.place(x=85, y=190)

    #bt_excluir.place(x=85, y=230)
    
    def mostrar_login():
        
        app_nome = Label(frame_tabela, text="Login", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # Definição do cabeçalho
        list_header = ['ID','Usuario' ]
    
        # Obtém os dados do estoque
        df_list = ver_login() # Certifique-se de que essa função retorna os dados corretamente
    
        global tree_login
    
        # Criando a Treeview
        tree_login = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

        # Barras de rolagem
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_login.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_login.xview)  # Corrigido aqui

        tree_login.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
        # Posicionando os widgets
        tree_login.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
    
        frame_Login.grid_rowconfigure(0, weight=12)

        # Configuração das colunas
        hd = ["nw", "nw"]
        h = [40,100]
    
        for n, col in enumerate(list_header):
            tree_login.heading(col, text=col.title(), anchor=NW)
            tree_login.column(col, width=h[n], anchor=hd[n])

        # Inserindo os dados
        if df_list:
            for item in df_list:
                    tree_login.insert("", "end", values=item)

    mostrar_login()

    l_titulo = Label(root1, text="Selecione o usuario na tabela, \n após o usuario selecionado, \n  clique no botão atualizar", font=('Ivy 10 bold'), bg=co0, fg=co1)
    l_titulo.place(x=175, y=370, anchor=CENTER)
#------------------------------------------------------------------------------------------------------------------------------------------------------
    
def painel_geral():
    
    
    global root
    
    #Criar uma nova janela
    root = Toplevel(root) 
    root.title("Painel de Controle")
    root.geometry("900x900")
    menubar = tk.Menu(root)  # Define the menubar
    root.config(menu=menubar)  # Attach the menubar to the root window
    #root.overrideredirect(1) 
    root.configure(background=co0)
    root.resizable(width=False, height=False)
    largura_root = 900
    altura_root = 900
    #obter tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root )//2
    pos_y = (altura_tela - altura_root)//2
    # Definir geometria da janela (LxA+X+Y)
    root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")
    
    def abrir_atualizacao():
        for widget in frame_painel.winfo_children():
         widget.destroy()
        atulizar() 
    def abrir_relatorio():
        for widget in frame_painel.winfo_children():
            widget.destroy()
        relatorio()
    def abrir_estoque():
        for widget in frame_painel.winfo_children():
            widget.destroy()
            estoque() 
    
    # Menu Estoque
    estoque = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Estoque", menu=estoque)
    estoque.add_command(label="Cadastrar Produto", command=abrir_estoque)
    estoque.add_command(label="Cadastrar Fornecedores", command=None)
    estoque.add_separator()
    estoque.add_command(label="Sair", command=root.destroy)  # Corrigido de add_cascade para add_command

    # Menu Relatórios
    relatorios = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Relatórios", menu=relatorios)
    relatorios.add_command(label="Gerar Relatórios", command=abrir_relatorio)  # Corrigido add_cascade para add_command

    # Menu Configurações
    configuracoes = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Configurações", menu=configuracoes)
    configuracoes.add_command(label="Atualizar o software", command=abrir_atualizacao)  # Corrigido "Atulizar" para "Atualizar"
    
    frame_painel = Frame(root, width=900, height=900, bg=co0)
    frame_painel.place(x=0, y=0)
    
    p_titulo = Label(frame_painel, text="Cadastro de Estoque ", font=('Ivy 20 bold'), bg=co0, fg=co1)
    p_titulo.place(x=450, y=400, anchor=CENTER)

    p_titulo = Label(frame_painel, text="Software destinado para  estoque.", font=('Ivy 10 '), bg=co0, fg=co1)
    p_titulo.place(x=450, y=500, anchor=CENTER)

    p_titulo = Label(frame_painel, text="Criado e desenvolvido por: VellosoDev. ", font=('Ivy 10 '), bg=co0, fg=co1)
    p_titulo.place(x=450, y=600, anchor=CENTER)
    
    
          

    def atulizar():
        
        # Função para verificar a atualização
        def verificar_atualizacao():
            
            label_status.config(text="Verificando por atualizações...")
            versao_atual = "1.0"  # Versão local (simulação)
            versao_remota = obter_versao_remota()  # Obtenha a versão remota
            if versao_remota > versao_atual:
                label_status.config(text=f"Nova versão {versao_remota} disponível! Clique em 'Atualizar'.")
                btn_atualizar.config(state="normal")
            else:
                label_status.config(text="Você já está na versão mais recente.")
                btn_atualizar.config(state="disabled")
                
        # Função para baixar a atualização e salvar na pasta de Downloads
        def baixar_atualizacao():
            url = "https://mega.nz/folder/7hgAxZ7I#SdwQCdwdDCrC80NQ3llQ5g"  # Insira aqui o URL real
            label_status.config(text="Baixando atualização...")
            btn_atualizar.config(state="disabled")
            
            try:
                # Caminho para a pasta Downloads
                pasta_downloads = Path(os.path.expanduser("~/Downloads"))
                arquivo_destino = pasta_downloads / "arquivo_atualizacao.exe"

                response = requests.get(url, stream=True)
                response.raise_for_status()  # Levanta exceção para erros HTTP
                total = int(response.headers.get('content-length', 0))
                
                # Escrevendo o arquivo enquanto atualiza o progresso
                with open(arquivo_destino, "wb") as arquivo:
                    baixado = 0
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            arquivo.write(chunk)
                            baixado += len(chunk)
                            progress_bar["value"] = (baixado / total) * 100
                            painel.update_idletasks()
        
                label_status.config(text=f"Download concluído! Arquivo salvo em {arquivo_destino}")
            except requests.exceptions.RequestException as e:
                label_status.config(text=f"Erro no download: {e}")
                
                # Função para obter a versão remota (a lógica pode ser ajustada para APIs)
        def obter_versao_remota():
                return "2.0"  # Simulação; implemente uma lógica real

        # Elementos da interface
        label_status = tk.Label(painel, text="Status: Aguardando...")
        label_status.pack(pady=10)

        btn_verificar = ttk.Button(painel, text="Verificar Atualização", command=verificar_atualizacao)
        btn_verificar.pack(pady=5)

        btn_atualizar = ttk.Button(painel, text="Fazer download agora", command=baixar_atualizacao, state="disabled")
        btn_atualizar.pack(pady=5)

        progress_bar = ttk.Progressbar(painel, mode="determinate")
        progress_bar.pack(pady=10)
        
 
 
          
       
def relatorio():
    
    frame_painel_r = Frame(root, width=900, height=900, bg=co0)
    frame_painel_r.place(x=0, y=0)
    
    
    # Definir a tabela (treeview)
    tree = ttk.Treeview(frame_painel_r, columns=("Produto", "Quantidade", "Categoria", "valor_total_Produto"), show="headings")
    tree.heading("Produto", text="Produto")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Categoria", text="Categoria")
    tree.pack()

    # Função para exibir o relatório
    def gerar_relatorio():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT produto, quantidade, categoria, valor_total_Produto FROM estoque")
        resultados = cursor.fetchall()
        conn.close()

        # Limpar a tabela antes de inserir novos dados
        for row in tree.get_children():
            tree.delete(row)

        # Inserir dados na tabela
        for produto, quantidade, categoria, valor_total_Produto  in resultados:
            tree.insert("", "end", values=(produto, quantidade, categoria, valor_total_Produto))

    # Função para gerar o gráfico
    def gerar_grafico():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT produto, quantidade, valor_total_Produto FROM estoque")
        resultados = cursor.fetchall()
        conn.close()

        if resultados:
            produtos = [row[0] for row in resultados]
            quantidades = [row[1] for row in resultados]

            # Criar o gráfico
            fig, ax = plt.subplots()
            ax.bar(produtos, quantidades, color="lightblue")
            ax.set_title("Estoque de Produtos")
            ax.set_xlabel("Produtos")
            ax.set_ylabel("Quantidade")

            # Exibir o gráfico no Tkinter
            canvas = FigureCanvasTkAgg(fig, master=frame_painel_r)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            messagebox.showinfo("Informação", "Nenhum dado disponível para gerar o gráfico.")

        # Frame para o relatório
        columns = ("Produto", "Quantidade", "Categoria", "valor total Produto")
        tree = ttk.Treeview(frame_painel_r, columns=columns, show="headings")
        tree.heading("Produto", text="Produto")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Categoria", text="Categoria")
        tree.heading("valor total Produto", text="valor total Produto")
        tree.pack(fill="both", expand=True)
    
    def executar_tarefas():
        gerar_relatorio()
        gerar_grafico()

    # Criando um botão unificado
    btn_unificado = ttk.Button(frame_painel_r, text="Gerar Tudo", command=executar_tarefas)
    btn_unificado.pack(pady=10)
        
    
    def estoque(): 
    
        frame_cad_titulo = Frame(root, width=900, height=50, bg=co0 )
        frame_cad_titulo.grid(row=0, column=0, sticky=NSEW)
    
        frame_cad_botoes = Frame(root, width=900, height=50, bg=co0 )
        frame_cad_botoes.grid(row=1, column=0, sticky=NSEW)
   
        frame_cad_produtos = Frame(root, width=900, height=300, bg=co0)
        frame_cad_produtos.grid(row=2, column=0, sticky=NSEW)
    
        frame_tabela = Frame(root, width=900, height=350, bg=co0)
        frame_tabela.grid(row=3, column=0, sticky=NSEW)

        l_titulo= Label(frame_cad_titulo, text="Cadastre novos Produtos", font=('Ivy 20 bold'), bg=co0, fg=co1)
        l_titulo.place(x=450, y=25, anchor=CENTER)
    
        def calcular_estoque(event=None):
            try:
                quantidade = int(e_quantidade.get())
                valor_unitario = float(e_preco_custo.get())
                total = quantidade * valor_unitario
                e_valor_total_Produto.delete(0, tk.END)  # Limpa o campo antes de exibir o novo valor
                e_valor_total_Produto.insert(0, f"{total:.2f}")  # Insere o valor calculado
            except ValueError:
                e_valor_total_Produto.delete(0, tk.END)  # Limpa o campo se houver erro
                e_valor_total_Produto.insert(0, "Erro")  # Mostra mensagem de erro
            
            
        # Função para buscar e exibir a soma dos valores no banco
        def atualizar_valor_total():
            try:
                # Conectar ao banco de dados
                conexao = sqlite3.connect("database.db")  # Substitua pelo caminho correto do banco
                cursor = conexao.cursor()

                # Consulta SQL para calcular a soma do valor total do estoque
                cursor.execute("SELECT SUM(valor_total_Produto) FROM estoque")
                resultado = cursor.fetchone()

                # Fecha a conexão com o banco
                conexao.close()

                # Define o valor atualizado ou 0.00 caso não haja registros
                valor_estoque = float(resultado[0]) if resultado[0] is not None else 0.00

                # Atualiza a Entry automaticamente
                e_valor_total_estoque.config(state="normal")
                e_valor_total_estoque.delete(0, tk.END)
                e_valor_total_estoque.insert(0, f"{valor_estoque:.2f}")  # Formato decimal
                e_valor_total_estoque.config(state="readonly")  # Bloqueia novamente

            except Exception as e:
                e_valor_total_estoque.config(state="normal")
                e_valor_total_estoque.delete(0, tk.END)
                e_valor_total_estoque.insert(0, f"Erro: {e}")  # Exibe erro na Entry
                e_valor_total_estoque.config(state="readonly")

             # Atualizar automaticamente o valor a cada 5 segundos
                def atualizar_automaticamente():
                    atualizar_valor_total()
                    root.after(5000, atualizar_automaticamente)  # Atualiza a cada 5 segundos

                    # Iniciar a atualização automática
                    atualizar_automaticamente()
    
    def novo_produto():
        
        fornecedor = c_fornecedor.get()
        produto = e_produto.get()
        quantidade = e_quantidade.get()
        categoria = c_categoria.get()
        preco_custo = e_preco_custo.get()
        valor_total_Produto = e_valor_total_Produto.get()
        ean = e_ean.get()
        valor_total_estoque = e_valor_total_estoque.get()
       
       
        lista =[fornecedor,produto,quantidade,categoria,preco_custo,valor_total_Produto,ean,valor_total_estoque]
        for i in lista:
            if i =='':
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return
            criar_estoque(lista)
            messagebox.showinfo('Sucesso', 'Os produtos inseridos com sucesso!')
           
        c_fornecedor.delete(0, END)
        e_produto.delete(0, END)
        e_quantidade.delete(0, END)
        c_categoria.delete(0, END)
        e_preco_custo.delete(0, END)
        e_valor_total_Produto.delete(0, END)
        e_ean.delete(0, END)
        e_valor_total_estoque.delete(0, END)
                 
        mostrar_produtos()
        
    def atualizar_produto():
        
        try:
            tree_itens = tree_estoque.focus()
            tree_dicionario = tree_estoque.item(tree_itens)
            tree_lista = tree_dicionario['values']
            
            valor_id = tree_lista[0]
        
            
            c_fornecedor.delete(0, END)
            e_produto.delete(0, END)
            e_quantidade.delete(0, END)
            c_categoria.delete(0, END)
            e_preco_custo.delete(0, END)
            e_valor_total_Produto.delete(0, END)
            e_ean.delete(0, END)
            e_valor_total_estoque.delete(0, END)
            
            c_fornecedor.insert(0, tree_lista[1])
            e_produto.insert(0, tree_lista[2])
            e_quantidade.insert(0, tree_lista[3])
            c_categoria.insert(0, tree_lista[4])
            e_preco_custo.insert(0, tree_lista[5])
            e_valor_total_Produto.insert(0, tree_lista[6])
            e_ean.insert(0, tree_lista[7])
            e_valor_total_estoque.insert(0, tree_lista[8])
            
            def update():
                
                fornecedor = c_fornecedor.get()
                produto = e_produto.get()
                quantidade = e_quantidade.get()
                categoria = c_categoria.get()
                preco_custo = e_preco_custo.get()
                valor_total_Produto = e_valor_total_Produto.get()
                ean = e_ean.get()
                valor_total_estoque = e_valor_total_estoque.get()
                
                lista= [fornecedor, produto,quantidade,categoria,preco_custo,valor_total_Produto,ean,valor_total_estoque, valor_id]
    
                atualizar_estoque(lista)
                messagebox.showinfo("Sucesso","Produto atualizado com sucesso!")
                
                c_fornecedor.delete(0, END)
                e_produto.delete(0, END)
                e_quantidade.delete(0, END)
                c_categoria.delete(0, END)
                e_preco_custo.delete(0, END)
                e_valor_total_Produto.delete(0, END)
                e_ean.delete(0, END)
                e_valor_total_estoque.delete(0,END)
            
                
                mostrar_produtos()
                botao_update.destroy()
                
            botao_update = Button(frame_cad_produtos, command= update,  anchor=CENTER,text='Salvar e Atualizar'.upper(), width=18, overrelief=RIDGE, font=('Ivy 7'), bg=co3, fg=co1)
            botao_update.place(x=710, y=130)  
        except IndexError:
            messagebox.showerror('Erro', 'Selecione os dados na tabela')
            
    def del_produto():
        try:
            tree_itens = tree_estoque.focus()
            tree_dicionario = tree_estoque.item(tree_itens)
            tree_lista = tree_dicionario['values']
            
            valor_id = tree_lista[0]
            
            # deletar dados no Banco de Dados
            deletar_estoque([valor_id])
            
            #Mostrando a menssagem de sucesso
            messagebox.showinfo('Sucesso', 'Produtos deletado com sucesso!')
            
            #mostrando os valores na tabela
            mostrar_produtos()
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos produto na tabela')
            
     #***********************************BOTÕES****************************************************************************************************************************************************************************
    
        
        app_add = Button(frame_cad_botoes,command=novo_produto,text="Adicionar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co0, fg=co1)
        app_add.place(x=10, y=10)

        app_img_delete = Image.open('img/delete.png')
    app_img_delete = app_img_delete.resize((18,18))
    app_img_delete = ImageTk.PhotoImage(app_img_delete)
    app_delete = Button(frame_cad_botoes,command=del_produto, image=app_img_delete, text="Excluir", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co0, fg=co1)
    app_delete.place(x=102, y=10)

    app_img_update = Image.open('img/update.png')
    app_img_update = app_img_update.resize((18,18))
    app_img_update = ImageTk.PhotoImage(app_img_update)
    app_update = Button(frame_cad_botoes,command=atualizar_produto, image=app_img_update, text="Atualizar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co0, fg=co1)
    app_update.place(x=194, y=10)

    
    app_procurar = Button(frame_cad_botoes, text="Procurar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co0, fg=co1)
    app_procurar.place(x=286, y=10)
    
    app_img_imprimir = Image.open('img/imprimir.png')
    app_img_imprimir = app_img_imprimir.resize((18,18))
    app_img_imprimir = ImageTk.PhotoImage(app_img_imprimir)
    app_imprimir = Button(frame_cad_botoes, image=app_img_imprimir, text="Imprimir", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co0, fg=co1)
    app_imprimir.place(x=378, y=10)
    
    #*************LABEL*****************************************************************************************
   
   
    a_id = Label(frame_cad_produtos, text="Id:", font=('Ivy 10 bold'), bg=co0,fg=co1)
    a_id.place(x=10, y=40)
    e_id = Entry(frame_cad_produtos, width=10, justify=LEFT, font=('Ivy 10 bold'), highlightthickness=1, relief="solid")
    e_id.place(x=38, y=40)

    a_produto = Label(frame_cad_produtos, text="Produto:", font=('Ivy 10 bold'), bg=co0,fg=co1)
    a_produto.place(x=10, y=80)
    e_produto = Entry(frame_cad_produtos, width=50, justify=LEFT, font=('Ivy 10 bold'), highlightthickness=1, relief="solid")
    e_produto.place(x=95, y=80)
    
    a_quantidade = Label(frame_cad_produtos, text="Quantidade:", font=('Ivy 10 bold'), bg=co0,fg=co1)
    a_quantidade.place(x=10, y=120)
    e_quantidade = Entry(frame_cad_produtos, width=50, justify=LEFT, font=('Ivy 10 bold'), highlightthickness=1, relief="solid")
    e_quantidade.bind("<KeyRelease>", calcular_estoque) 
    e_quantidade.place(x=95, y=120)
    
    c_categoria = ttk.Combobox(frame_cad_produtos, width=18, font=('Ivy 8 bold'))
    c_categoria.set('Categorias')
    c_categoria['values'] = ver_categoria()
    c_categoria.place(x=220, y=10)
    
    a_preco_custo = Label(frame_cad_produtos, text="Preço de Custo (R$):", font=('Ivy 10 bold'), bg=co0,fg=co1)
    a_preco_custo.place(x=10, y=160)
    e_preco_custo = Entry(frame_cad_produtos ,width=20, justify=LEFT, font=('Ivy 10 bold'), highlightthickness=1, relief="solid")
    e_preco_custo.bind("<KeyRelease>", calcular_estoque) 
    e_preco_custo.place(x=145, y=160)

    a_valor_total_Produto = Label(frame_cad_produtos, text="Valor total em estoque por produto:(R$):", font=('Ivy 10 bold'), bg=co0,fg=co1)
    a_valor_total_Produto.place(x=10, y=200)
    e_valor_total_Produto = Entry(frame_cad_produtos,width=20,state="normal", justify=LEFT, font=('Ivy 10 bold'), highlightthickness=1, relief="solid")
    e_valor_total_Produto.place(x=265, y=200)

    a_valor_total_estoque = Label(frame_cad_produtos, text="Valor Total em estoque(R$):", font=('Ivy 10 bold'), bg=co0,fg=co1)
    a_valor_total_estoque.place(x=10, y=240)
    e_valor_total_estoque = Entry(frame_cad_produtos, state="readonly", width=20, justify=LEFT, font=('Ivy 10 bold'), highlightthickness=1, relief="solid")
    e_valor_total_estoque.place(x=200, y=240)

    a_ean = Label(frame_cad_produtos, text="EAN:", font=('Ivy 10 bold'), bg=co0,fg=co1)
    a_ean.place(x=370, y=10)
    e_ean = Entry(frame_cad_produtos, width=20, justify=LEFT, font=('Ivy 10 bold'), highlightthickness=1, relief="solid")
    e_ean.place(x=410, y=10)
    
    #Pegando as Fornecedores
    fornecedores = Ver_fornecedor()  # Fetches supplier data.
    # Extract the second element (index 1) from each entry in fornecedores.
    lista_fornecedores = [i[2] for i in fornecedores]
    # Create the Combobox.
    c_fornecedor = ttk.Combobox(frame_cad_produtos, width=30, font=('Ivy 8 bold'))
    c_fornecedor['values'] = lista_fornecedores  # Set the list of options.
    c_fornecedor.set(lista_fornecedores[0] if lista_fornecedores else "Fornecedores")  # Set the default value.
    c_fornecedor.place(x=10, y=10)  # Define its position.
    
    def mostrar_produtos():
        
        app_nome = Label(frame_tabela, text="Tabela de Produtos", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # Definição do cabeçalho
        list_header = ['id', 'fornecedor', 'produto', 'quantidade', 'categoria',  'preco_custo','valor_total_Produto', 'valor_total_em_estoque', 'ean']
    
        # Obtém os dados do estoque
        df_list = ver_estoque()  # Certifique-se de que essa função retorna os dados corretamente
    
        global tree_estoque
    
        # Criando a Treeview
        tree_estoque = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

        # Barras de rolagem
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_estoque.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_estoque.xview)  # Corrigido aqui

        tree_estoque.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
        # Posicionando os widgets
        tree_estoque.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
    
        frame_tabela.grid_rowconfigure(0, weight=12)

        # Configuração das colunas
        hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
        h = [40, 150, 150, 70, 70, 150, 150, 100,100 ]
    
        for n, col in enumerate(list_header):
            tree_estoque.heading(col, text=col.title(), anchor=NW)
            tree_estoque.column(col, width=h[n], anchor=hd[n])

        # Inserindo os dados
        if df_list:
            for item in df_list:
                tree_estoque.insert("", "end", values=item)
    mostrar_produtos()
  
        

    
       

   

    
    
    
    
     
    
    
    
    
    
       
 


login()
root.mainloop()