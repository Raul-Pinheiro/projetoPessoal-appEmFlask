from  configs.setup import *


@app.route("/")
def home():
    """ Pagina principal do portal"""    
    title='Home'   
    return render_template('home.html', title=title)

@app.route("/edita/<int:id_user>")

def edita(id_user):

    db_user = User(db_name)
    values=db_user.pegaUserPorID(id_user)
    title='Edita Usuário'   
    print(id_user)
    return render_template('edita.html',title=title,values=values)

