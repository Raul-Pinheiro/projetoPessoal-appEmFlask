from flask import Flask, render_template,request,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy



#Application config
app = Flask(__name__,template_folder='../templates',static_folder='../static')


#Database config
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql:iluvatar96@localhost/db_flaskApp'




