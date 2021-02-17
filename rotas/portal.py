from  app.app import *

@app.route("/dashboard")
def dashboard():
    """ Dashboard do portal """
    title='Dashboard'
    return render_template('dashboard.html', title=title)



    
