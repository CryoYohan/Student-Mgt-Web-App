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

<<<<<<< HEAD

@app.route("/userregister",methods=['POST'])
=======
@app.route("/register")
def register():
    return render_template("register.html",pagetitle="REGISTER")

@app.route("/userlogin",methods=['POST'])
>>>>>>> d415e64e731f1483a43a14f2280e77146f9cf82e
def userlogin()->None:
    username:str = request.form['username']
    password:str = request.form['password']
    if username == "admin" and password=="user":
        flash("LOGIN SUCCESSFUL!")
        return redirect(url_for("landingpage"))
    else:
        flash("LOGIN FAILED!")
        return redirect(url_for("login"))


@app.route("/userlogin",methods=['POST'])
def userlogin()->None:
    username:str = request.form['username']
    password:str = request.form['password']
    if username == "admin" and password=="user":
        return redirect(url_for("landingpage"))
    else:
        return redirect(url_for("login"))

@app.route("/register")
def register():
    return render_template("register.html", pagetitle="Register",shownavbar=False)


@app.route("/login")
def login()->None:
    return render_template("login.html",pagetitle='user login',shownavbar=False)

@app.route("/")
def landingpage():
    return render_template("landingpage.html",pagetitle='Tidert\'s University',shownavbar=True)

@app.route("/showstudents")
def show()->None:
    current_url = request.path
    return render_template("show.html",slist = students,pagetitle='student list', shownavbar=True)


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")