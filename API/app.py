from flask import Flask, request, jsonify
from conexao import Conexao  # Importando a classe Conexao

app = Flask(__name__)

# Configuração do banco de dados MySQL
db_config = {
    "host": "localhost",  # Altere se necessário
    "user": "seu_usuario",
    "password": "sua_senha",
    "database": "seu_banco"
}

@app.route('/api/get/login', methods=['GET'])
def login():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')

    if not usuario or not senha:
        return jsonify({"status": "erro", "mensagem": "Usuário e senha são obrigatórios!"}), 400

    # Criando instância da classe Conexao e verificando o usuário
    conexao = Conexao(db_config)
    if conexao.verificar_usuario(usuario, senha):
        return jsonify({"status": "sucesso", "mensagem": "Login realizado com sucesso!"})
    else:
        return jsonify({"status": "erro", "mensagem": "Usuário ou senha inválidos!"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
