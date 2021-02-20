from flask import Flask, render_template,request,redirect,session,flash
from flask.globals import g
from database.models import *


#Application config
app = Flask(__name__,template_folder='../assets/templates',static_folder='../assets/static')
app.secret_key='segredo'
app.config['DATABASE_URI']= 'postgres://postgres:iluvatar96@localhost:5432/bancoDados'
db_name = 'bancoDados'

# PSYCOPG2_TESTDB
# PSYCOPG2_TESTDB_HOST
# PSYCOPG2_TESTDB_PORT
# PSYCOPG2_TESTDB_USER









