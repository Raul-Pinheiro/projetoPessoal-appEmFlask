import sqlite3
import os

class ListaUser:
    def __init__(self,id,user,pw):
        self.id = id
        self.user = user
        self.pw = pw

class Database():
    def __init__(self,db_name):     
        self.db_name = db_name     
    
    def iniciaBanco(self):                   
        con = sqlite3.connect(self.db_name)
        print(self.db_name)
        return con


class User(): 
    
    def __init__(self,db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()
        
    def createTable(self):
        
        self.con.cursor().execute(
            'CREATE TABLE IF NOT EXISTS tb_usuario (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            user VARCHAR(15) NOT NULL,\
            password VARCHAR(100) NOT NULL)')        
        
    def insertUser(self,user,pw):
        self.user = user
        self.pw =pw 
        
        self.con.cursor().execute("INSERT INTO 'tb_usuario'\
            (user,password) VALUES ('{}','{}')".format(self.user,self.pw))
        self.con.commit()
        self.cur.close()
        self.con.close()
             
    def selectUsers(self):
            
        self.cur.execute('SELECT * FROM tb_usuario')

        usuarios =[]
        for row in self.cur.fetchall():
                        
            linha = ListaUser(row[0],row[1],row[2])
            usuarios.append(linha)
        return usuarios

    def deleteUsers(self,id):       
        
        self.cur.execute('DELETE FROM tb_usuario WHERE id={}'.format(id))
        self.con.commit()
        
    def updateUsers(self,id,user,pw):
        self.id=id
        self.user=user
        self.pw=pw
        
        self.cur.execute("""
        UPDATE 'tb_usuario' 
        SET user =?, password =?
        WHERE id = ?
        """,(self.user,self.pw,self.id))
        self.con.commit()
    

    def pegaUserPorID(self,id):
        self.id = id
        self.cur.execute('SELECT * FROM tb_usuario WHERE id = {}'.format(self.id))
        usuario = []

        for item in self.cur.fetchone():
            usuario.append(item)

        return usuario

        
        