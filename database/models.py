import pg8000 

class ListaUser:
    def __init__(self,id,user,pw):
        self.id = id
        self.user = user
        self.pw = pw

class ConnectUserTable():
    def __init__(self):   
        self.con = pg8000.connect("postgres",host="localhost",database="bancoDados",\
            port=5432,password="iluvatar96",unix_sock=None,ssl_context=None,timeout=None,\
            tcp_keepalive=True,application_name=None,replication=None)
        self.cur = self.con.cursor()

    def createTable(self):        
        self.cur.execute("CREATE TABLE IF NOT EXISTS tb_clientes (id_user SERIAL PRIMARY KEY,\
            usuario VARCHAR(15) NOT NULL, senha VARCHAR(15) NOT NULL)")
        self.con.commit()
        
    
    def insertUser(self,user,pw):
        self.user = user
        self.pw = pw
        self.cur.execute("INSERT INTO tb_clientes (usuario,senha) VALUES ('{}','{}')".format(self.user,self.pw)) 
        self.con.commit()
        self.cur.close()
        self.con.close()

 
                
    def selectUsers(self):
            
        self.cur.execute('SELECT * FROM tb_clientes')

        usuarios =[]
        for row in self.cur.fetchall():
                        
            linha = ListaUser(row[0],row[1],row[2])
            usuarios.append(linha)
        return usuarios

    def deleteUsers(self,id):       
        self.id =id 
        self.cur.execute("DELETE FROM tb_clientes WHERE id_user={}".format(self.id))
        self.con.commit()

    def updateUsers(self,id,user,pw):
        self.id=id
        self.user=user
        self.pw=pw
        
        self.cur.execute("""
        UPDATE 'tb_clientes' 
        SET usuario =?, senha =?
        WHERE id_user = ?
        """,(self.user,self.pw,self.id))
        self.con.commit()
    
    def pegaUserPorID(self,id):
        self.id = id
        self.cur.execute('SELECT * FROM tb_clientes WHERE id_user = {}'.format(self.id))
        usuario = []

        for item in self.cur.fetchone():
            usuario.append(item)

        return usuario



