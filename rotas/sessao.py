from  app.app import *


@app.route("/login", methods=['POST'])
def login():
    """ Rotas de acesso ao banco de autenticação do portal"""
    user = request.form['home_user']
    pw = request.form['home_password']
    if 'username' == user:
        return redirect('/dashboard')
    
    else:
        return redirect('/')
    