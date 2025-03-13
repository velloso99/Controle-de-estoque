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





root.mainloop()