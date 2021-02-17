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
        self.con.cursor().close()
        self.con.close()
             


        
        