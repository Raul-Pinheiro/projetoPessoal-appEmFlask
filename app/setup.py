from flask import Flask, render_template,request,redirect,session,flash,g
from flask.globals import g
from models.models import *
import sqlite3



#Application config
app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.secret_key='segredo'

db = Database('dao.db')

objUsuario= User(db.db_name)
objUsuario.createTable()  
# app.database = 'db_flaskApp.db'








