import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("500x400")
root.resizable(False, False)

# Carregar imagem (somente PNG/GIF)
imagem = tk.PhotoImage(file="imgs/logotipo.png")  # Substitua "imagem.png" pelo nome correto do arquivo

# Label do título
tk.Label(root, text="Área Administrativa", font=("Arial Black", 14, "bold")).pack(pady=5)

# Label para exibir a imagem
tk.Label(root, image=imagem).pack(pady=10)

# Restante da interface
tk.Label(root, text="Usuário:", font=("Arial", 12)).pack(pady=5)
entrada_usuario = tk.Entry(root)
entrada_usuario.pack(pady=5)

tk.Label(root, text="Senha:", font=("Arial", 12)).pack(pady=5)
entrada_senha = tk.Entry(root, show="*")
entrada_senha.pack(pady=5)

tk.Button(root, text="Entrar", font=("Arial", 12)).pack(pady=15)

root.mainloop()
