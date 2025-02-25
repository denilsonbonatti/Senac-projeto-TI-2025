from flask import Flask, request, jsonify
from conexao import Conexao

app = Flask(__name__)

# Configurações do Banco de Dados
db_config = {
    "host": "172.24.246.169",
    "user": "App",
    "password": "Senha123",
    "database": "EMPRESA"
}

@app.route('/get/login/', methods=['POST'])
def verificar_usuario():
    dados = request.get_json()
    usuario = dados.get('usuario')
    senha = dados.get('senha')

    try:
        conexao = Conexao(db_config)
        usuario_existe = conexao.verificar_usuario(usuario, senha)
        return jsonify({"usuario_existe": usuario_existe}), 200 if usuario_existe else 401

    except Exception as e:
        return jsonify({"erro": f"Falha ao conectar ao banco: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
