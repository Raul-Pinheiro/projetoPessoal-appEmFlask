from flask import Flask, render_template

app = Flask(__name__,template_folder='../templates',static_folder='../static')

@app.route("/")
def home():
    title='Home' 
    return render_template('home.html', title=title)


@app.route("/dashboard")
def dashboard():

    title='Dashboard' 

    return render_template('dashboard.html', title=title)