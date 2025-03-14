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
    painel = Toplevel(root) 
    painel.title("Painel de Controle")
    painel.geometry("900x900")
    menubar = tk.Menu(painel)  # Define the menubar
    painel.config(menu=menubar)  # Attach the menubar to the root window
    #root.overrideredirect(1) 
    painel.configure(background=co0)
    painel.resizable(width=False, height=False)
    largura_root = 900
    altura_root = 900
    #obter tamanho da tela
    largura_tela = painel.winfo_screenwidth()
    altura_tela = painel.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root )//2
    pos_y = (altura_tela - altura_root)//2
    # Definir geometria da janela (LxA+X+Y)
    painel.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")
    
    def abrir_atualizacao():
        for widget in frame_painel.winfo_children():
         widget.destroy()
        atulizar()
   
    # Menu Estoque
    estoque = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Estoque", menu=estoque)
    estoque.add_command(label="Cadastrar Produto", command=None)
    estoque.add_command(label="Cadastrar Fornecedores", command=None)
    estoque.add_separator()
    estoque.add_command(label="Sair", command=root.destroy)  # Corrigido de add_cascade para add_command

    # Menu Relatórios
    relatorios = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Relatórios", menu=relatorios)
    relatorios.add_command(label="Gerar Relatórios", command=relatorio)  # Corrigido add_cascade para add_command

    # Menu Configurações
    configuracoes = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Configurações", menu=configuracoes)
    configuracoes.add_command(label="Atualizar o software", command=abrir_atualizacao)  # Corrigido "Atulizar" para "Atualizar"
    
    frame_painel = Frame(root, width=900, height=900, bg=co0 )
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
    
    
    #Criar uma nova janela
    painel = Toplevel(root) 
    painel.title("Painel de Controle")
    painel.geometry("900x900")
    menubar = tk.Menu(painel)  # Define the menubar
    painel.config(menu=menubar)  # Attach the menubar to the root window
    #root.overrideredirect(1) 
    painel.configure(background=co0)
    painel.resizable(width=False, height=False)
    largura_root = 900
    altura_root = 900
    #obter tamanho da tela
    largura_tela = painel.winfo_screenwidth()
    altura_tela = painel.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root )//2
    pos_y = (altura_tela - altura_root)//2
    # Definir geometria da janela (LxA+X+Y)
    painel.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")
    
    # Definir a tabela (treeview)
    tree = ttk.Treeview(painel, columns=("Produto", "Quantidade", "Categoria", "valor_total_Produto"), show="headings")
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
            canvas = FigureCanvasTkAgg(fig, master=painel)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            messagebox.showinfo("Informação", "Nenhum dado disponível para gerar o gráfico.")

        # Frame para o relatório
        columns = ("Produto", "Quantidade", "Categoria", "valor total Produto")
        tree = ttk.Treeview(painel, columns=columns, show="headings")
        tree.heading("Produto", text="Produto")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Categoria", text="Categoria")
        tree.heading("valor total Produto", text="valor total Produto")
        tree.pack(fill="both", expand=True)
    
    def executar_tarefas():
        gerar_relatorio()
        gerar_grafico()

    # Criando um botão unificado
    btn_unificado = ttk.Button(painel, text="Gerar Tudo", command=executar_tarefas)
    btn_unificado.pack(pady=10)
        
    
        

   

    
    
    
    
     
    
    
    
    
    
       
 


login()
root.mainloop()