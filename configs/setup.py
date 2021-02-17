from flask import Flask, render_template,request,redirect,session,flash
from flask.globals import g
from database.models import *


#Application config
app = Flask(__name__,template_folder='../assets/templates',static_folder='../assets/static')
app.secret_key='segredo'

db = Database('dao.db')

# usuarios= User(db.db_name)
# usuarios.createTable()  
# app.database = 'db_flaskApp.db'








