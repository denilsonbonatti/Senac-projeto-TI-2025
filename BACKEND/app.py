from conexao import Conexao

#Configurações do Banco de Dados

db_config = {
    "host": "192.168.113.30",
    "user": "App",
    "password": "Senha123",
    "database": "EMPRESA"
}
#Criando conexão com o banco de dados
conexao = Conexao(db_config)
conexao.conectar()
conexao.verificar_usuario('email@email.com', 'Senha123')