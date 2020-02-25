from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '[+] server start running.!'

@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/add')
def add_page():
    return render_template('add.html')

@app.route('/500')
def e500_page():
    return render_template('500.html')

@app.route('/401')
def e401_page():
    return render_template('401.html')

@app.route('/404')
def e404_page():
    return render_template('404.html')            
	
if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)