from  app.setup import *


@app.route("/cadastro", methods=['POST'])
def cadastro():
    """ Rotas de acesso ao banco de autenticação do portal"""
    if request.method=='POST':
        user = request.form['home_user']
        pw = request.form['home_password']
    
        if user =='' or pw=='':
            return redirect('/')
        else:
            objUsuario= User(db.db_name)
            objUsuario.createTable()    
            objUsuario.insertUser(user,pw)
    
        return redirect('/views')
    
    else:
        return redirect('/')

@app.route("/views")
def views():
    """ Dashboard do portal """
    title='Dashboard'
    
    con = sqlite3.connect(db.db_name)
    cur = con.cursor()
    cur.execute('SELECT * FROM tb_usuario')

    usuarios =[]
    for row in cur.fetchall():
                        
        linha = ListaUser(row[0],row[1],row[2])
        usuarios.append(linha)
        
    
    return render_template('dashboard.html', title=title, usuarios=usuarios)


@app.route("/delUser/<int:id_user>")
def delUser(id_user):
    con = sqlite3.connect(db.db_name)
    cur = con.cursor()
    cur.execute('DELETE FROM tb_usuario WHERE id={}'.format(id_user))
    con.commit()

    return redirect('/dashboard')
    