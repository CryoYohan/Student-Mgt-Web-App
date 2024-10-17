from flask import Flask,render_template,request,url_for,redirect,flash

app = Flask(__name__)
app.secret_key="!@#!@#"

students:list = [
    {'idno':'0001','lastname':'durano','firstname':'dennis','course':'bscpe','level':'4',},
    {'idno':'0002','lastname':'india','firstname':'alpha','course':'bscs','level':'2',},
    {'idno':'0003','lastname':'hotel','firstname':'bravo','course':'bsit','level':'4',},
    {'idno':'0004','lastname':'golf','firstname':'delta','course':'bsba','level':'3',},
    {'idno':'0005','lastname':'foxtrot','firstname':'echo','course':'bscs','level':'3',},
]

@app.route("/register")
def register():
    return render_template("register.html",pagetitle="REGISTER")

@app.route("/userlogin",methods=['POST'])
def userlogin()->None:
    username:str = request.form['username']
    password:str = request.form['password']
    if username == "admin" and password=="user":
        flash("LOGIN SUCCESSFUL!")
        return redirect(url_for("landingpage"))
    else:
        flash("LOGIN FAILED!")
        return redirect(url_for("login"))


@app.route("/login")
def login()->None:
    return render_template("login.html",pagetitle='user login')

@app.route("/")
def landingpage():
    return render_template("landingpage.html",pagetitle='Student Management Web App')


@app.route("/index")
def index()->None:
    return render_template("index.html",slist = students,pagetitle='student list')
    
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")