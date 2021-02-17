from  configs.setup import *



@app.route("/cadastro", methods=['POST'])
def cadastro():
    """ Rotas de acesso ao banco de autenticação do portal"""
    if request.method=='POST':

        user = request.form['home_user']
        pw = request.form['home_password']
    
        if user =='' or pw=='':
            return redirect('/')
        else:
            db_user =User(db.db_name)
            db_user.createTable()    
            db_user.insertUser(user,pw)  

        return redirect('/views')
    
    else:
        
        return redirect('/')

@app.route("/views")
def views():
    """ Dashboard do portal """

    title='Views'
    db_user = User(db.db_name)       
    
    return render_template('dashboard.html', title=title, usuarios=db_user.selectUsers())


@app.route("/delUser/<int:id_user>")
def delUser(id_user):    
    db_user = User(db.db_name)
    db_user.deleteUsers(id_user) 
     
    return redirect('/views')


@app.route("/editaUser", methods=['POST',])
def editaUser():
    if request.method=="POST":
        id=request.form['home_id_edit']
        user= request.form['home_user_edit']
        pw=request.form['home_password_edit']

        db_user = User(db.db_name)
        db_user.updateUsers(id,user,pw)

    return redirect('/views')
    