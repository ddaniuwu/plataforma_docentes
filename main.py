from flask import Flask , render_template , request
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
#from  service.controller_users import insertar_usuario
#from service.database import obtener_conexion


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/login')
def index():
    return render_template('index.html')



@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/home/search')
def search():
    return render_template('search.html')



@app.route('/home/graphics2')
def graphics2():
    return render_template('graphics2.html')


@app.route('/home/camera')
def camera():
    return render_template('camera.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')