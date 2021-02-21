from flask import Flask, render_template,request,redirect,session,flash



#Application config
app = Flask(__name__,template_folder='../assets/templates',static_folder='../assets/static')
app.secret_key='iluvatar96'



# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:iluvatar96@localhost:5432/bancoDados'






