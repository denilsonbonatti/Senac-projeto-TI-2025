import tkinter as tk
from tkinter import messagebox
import tela_inclusao_usuarios
#import tela_alteracao_usuarios
#import tela_consulta_usuarios
#import tela_exclusao_usuarios
#import tela_inclusao_produtos
#import tela_alteracao_produtos
#import tela_consulta_produtos
#import tela_exclusao_produtos

def abrir_tela_menu():

    def abrir_tela_inclusao_usuarios():
        tela_inclusao_usuarios.criar_tela_inclusao_usuarios()

    def abrir_tela_alteracao_usuarios():
        tela_alteracao_usuarios.criar_tela_alteracao_usuarios()

    def abrir_tela_consulta_usuarios():
        tela_consulta_usuarios.criar_tela_consulta_usuarios()

    def abrir_tela_exclusao_usuarios():
        tela_exclusao_usuarios.criar_tela_exclusao_usuarios()

    def abrir_tela_inclusao_produtos():
        tela_inclusao_produtos.criar_tela_inclusao_produtos()

    def abrir_tela_alteracao_produtos():
        tela_alteracao_produtos.criar_tela_alteracao_produtos()

    def abrir_tela_consulta_produtos():
        tela_consulta_produtos.criar_tela_consulta_produtos()

    def abrir_tela_exclusao_produtos():
        tela_exclusao_produtos.criar_tela_exclusao_produtos()

    def sair():
        resposta = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
        if resposta:
            root.destroy()

    root = tk.Tk()
    root.title("Menu Principal")

    # Maximizar a janela
    root.state('zoomed')

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    menu_usuarios = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Usuários", menu=menu_usuarios)
    menu_usuarios.add_command(label="Inclusão", command=abrir_tela_inclusao_usuarios)
    menu_usuarios.add_command(label="Alteração", command=abrir_tela_alteracao_usuarios)
    menu_usuarios.add_command(label="Consulta", command=abrir_tela_consulta_usuarios)
    menu_usuarios.add_command(label="Exclusão", command=abrir_tela_exclusao_usuarios)

    menu_produtos = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Produtos", menu=menu_produtos)
    menu_produtos.add_command(label="Inclusão", command=abrir_tela_inclusao_produtos)
    menu_produtos.add_command(label="Alteração", command=abrir_tela_alteracao_produtos)
    menu_produtos.add_command(label="Consulta", command=abrir_tela_consulta_produtos)
    menu_produtos.add_command(label="Exclusão", command=abrir_tela_exclusao_produtos)

    menu_bar.add_command(label="Sair", command=sair)

    root.mainloop()