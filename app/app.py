from flask import Flask , render_template,request , redirect,jsonify,flash,url_for
import config
app = Flask(__name__)

@app.route("/ok")
def sys_check():
    '''this function tell that falsk server is ok and running!!'''
    ret = {'status':'ok','message':'[+] flask server is running'}
    return jsonify(ret) , 200

@app.route('/index')
def index():    
    return render_template('index.html')

@app.route('/',methods=["GET", "POST"])
def login():
    '''this function return login page'''
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["Password"]
        if check(username,password):
            return redirect(url_for('index'))
        else:
            error = '!!!یوزر نامعتبر!!!' 
               
    return render_template('login.html', error=error)

@app.route('/add',methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        name = request.form["name"]
        titlew = request.form["titlew"]
        message = request.form["message"]
        #print("[+] new work gotted ")
        #print("[+] writer is : %s" % name)
        #print("[+] work title is : %s" % titlew)
        #print("[+] work message is : %s" % message)
        return redirect('index')

    else:
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

def check(username,password):
    res = False
    if username == config.usernamein and password == config.passwordin:
        res = True
    return res               
	
if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)
    