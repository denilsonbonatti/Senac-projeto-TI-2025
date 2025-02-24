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