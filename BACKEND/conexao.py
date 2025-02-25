import mysql.connector


class Conexao:
    def __init__(self, config):
        self.config = config
        self.conexao = None
        self.cursor = None
    
    def conectar(self):
        try:
            if self.conexao is None or not self.conexao.is_connected():
                self.conexao = mysql.connector.connect(**self.config)
                self.cursor = self.conexao.cursor(dictionary=True)
        except mysql.connector.Error as err:
            return(f"Erro ao conectar ao banco de dados: {err}")   
    
    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
    
    def consultar(self, query, params=None):
        self.conectar()
        if self.conexao is not None:
            self.cursor.execute(query, params)
            resultado = self.cursor.fetchone()
            self.desconectar()
            return resultado
        
    def verificar_usuario(self, email, senha):
        query = "SELECT * FROM adm_users WHERE email = %s AND senha = %s"
        resultado = self.consultar(query, (email, senha))
        return resultado is not None
