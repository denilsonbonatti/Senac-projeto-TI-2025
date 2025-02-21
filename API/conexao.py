import mysql.connector

class Conexao:
    def __init__(self, config):
        self.config = config
        self.conexao = None
        self.cursor = None

    def conectar(self):
        if self.conexao is None or not self.conexao.is_connected():
            self.conexao = mysql.connector.connect(**self.config)
            self.cursor = self.conexao.cursor(dictionary=True)

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()

    def consultar(self, query, params=None):
        self.conectar()
        self.cursor.execute(query, params)
        resultado = self.cursor.fetchone()
        self.desconectar()
        return resultado

    def verificar_usuario(self, usuario, senha):
        query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s"
        resultado = self.consultar(query, (usuario, senha))
        return resultado is not None  # Retorna True se o usuário for encontrado
