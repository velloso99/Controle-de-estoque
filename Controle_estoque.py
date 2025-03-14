from mold import*


#Criando a janela
root = tk.Tk()
root.title("Controle de Estoque")
root.geometry("500x300")
root.configure(background=co0)
root.resizable(width=False, height=False)
#root.overrideredirect(1)
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
            
            root.destroy()
            painel_geral()
            
        else:
            messagebox.showerror("Erro", "Usuario ou senha incorretos!")
        cursor.close()
        
    
        root.destroy() 
    
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
    
    bt_esqueceu = Button(frame_login, command=None , text="Esqueceu a Senha", bd=3, bg=co0, fg=co1, font=('verdana', 11, 'bold'))
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
        
        
        

























def painel_geral():
    pass


login()
root.mainloop()