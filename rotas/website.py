from  app.app import *


@app.route("/")
def home():
    """ Pagina principal do portal"""
    title='Home' 
    return render_template('home.html', title=title)