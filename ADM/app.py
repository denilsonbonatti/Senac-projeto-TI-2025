import tkinter as tk
from tkinter import messagebox
import requests 

root = tk.Tk()
root.title("Área de Login")
root.geometry("500x400")
root.resizable(False, False)

def verifica_usuario():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    url_api = "http://10.105.44.35:5000/get/login/"  # Corrigida a URL
    response = requests.post(url_api, json={"usuario": usuario, "senha": senha})
    
    if response.status_code == 200:
        data = response.json()
        if data.get("usuario_existe"):
            abrir_menu_crud()
    else:
        messagebox.showerror("Login Inválido", "Usuário ou senha inválidos.")

def abrir_menu_crud():
    print("Aqui será o menu do CRUD!!!")

tk.Label(root, text="Área administrativa", font=("Arial Black", 14, "bold")).pack(pady=5)

try:
    imagem = tk.PhotoImage(file="ADM/imgs/logotipo.png")
    tk.Label(root, image=imagem).pack(pady=10)
except Exception as e:
    print(f"Erro ao carregar imagem: {e}")

tk.Label(root, text="Usuário:", font=("Arial", 12)).pack(pady=5)
entrada_usuario = tk.Entry(root, width=40)
entrada_usuario.pack(pady=5)

tk.Label(root, text="Senha:", font=("Arial", 12)).pack(pady=5)
entrada_senha = tk.Entry(root, show="*")
entrada_senha.pack(pady=5)

tk.Button(root, text="Entrar", font=("Arial", 12), command=verifica_usuario).pack(pady=15)

root.mainloop()
