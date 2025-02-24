import tkinter as tk

root = tk.Tk()
root.title("Área de Login")
root.geometry("500x400")
root.resizable(False,False)

# Label do título
tk.Label(root, text="Área administrativa", font=("Arial Black", 14, "bold")).pack(pady=5)

# Carrega imagem
imagem = tk.PhotoImage(file="ADM/imgs/logotipo.png")

# Label para exibir imagem

tk.Label(root, image=imagem).pack(pady=10)

#Restante da interface

tk.Label(root, text="Usuário:", font=("Arial", 12)).pack(pady=5)
entrada_usuario = tk.Entry(root, width=40)
entrada_usuario.pack(pady=5)

tk.Label(root, text="Senha:", font=("Arial", 12)).pack(pady=5)
entrada_senha = tk.Entry(root, show="*")
entrada_senha.pack(pady=5)

tk.Button(root, text="Entrar", font=("Arial",12)).pack(pady=15)

root.mainloop()