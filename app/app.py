from flask import Flask , render_template,request , redirect
import config
app = Flask(__name__)

@app.route('/index.html')
def index_page():    
    return render_template('index.html')

@app.route('/login.html',methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["Password"]
        if check(username,password):
            return redirect('index.html')
        else:
            return redirect('401.html')    
    else:
        return render_template('login.html')

@app.route('/add.html',methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        name = request.form["name"]
        titlew = request.form["titlew"]
        message = request.form["message"]
        print("[+] new work gotted ")
        print("[+] writer is : %s" % name)
        print("[+] work title is : %s" % titlew)
        print("[+] work message is : %s" % message)
        return redirect('index.html')

    else:
        return render_template('add.html')

@app.route('/500.html')
def e500_page():
    return render_template('500.html')

@app.route('/401.html')
def e401_page():
    return render_template('401.html')

@app.route('/404.html')
def e404_page():
    return render_template('404.html')            
	
if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)

def check(username,password):
    res = False
    if username == config.username and password == config.password:
        res = True
    return res    