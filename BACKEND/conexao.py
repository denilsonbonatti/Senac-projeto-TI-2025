import mysql.connector

class Conexao:
    def __init__(self,config):
        self.config = config
        self.conexao = None
        self.cursor = None
    
    def conectar(self):
        try:
            if self.conexao is None or not self.conexao.is_connected():
                self.conexao = mysql.connector.connect(**self.config)
                self.cursor = self.conexao.cursor(dictionary=True)
                print("Ok!! Aleluia!!")

        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados:{err}")   
    
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
        print(resultado)
    
    def verificar_usuario(self, email, senha):
        query = "SELECT * FROM adm_users WHERE email = %s AND senha = %s"
        resultado = self.consultar(query, (email, senha))
        print (resultado)
