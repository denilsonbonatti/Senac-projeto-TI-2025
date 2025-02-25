from flask import Flask, request, jsonify
from conexao import Conexao

app = Flask(__name__)

# Configurações do Banco de Dados
db_config = {
    "host": "192.168.125.147",
    "user": "App",
    "password": "Senha123",
    "database": "EMPRESA"
}

@app.route('/get/login/', methods=['POST'])
def verificar_usuario():
    dados = request.get_json()
    usuario = dados.get('usuario')
    senha = dados.get('senha')

    conexao = Conexao(db_config)
    usuario_existe = conexao.verificar_usuario(usuario, senha)
    print (jsonify({"usuario_existe": usuario_existe}), 200 if usuario_existe else 401)
    return jsonify({"usuario_existe": usuario_existe}), 200 if usuario_existe else 401
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
