from flask import Flask,render_template,request,url_for,redirect,flash
from dbhelper import Databasehelper
from student import Student
from hashpw import PasswordHashing

app = Flask(__name__)
db = Databasehelper()
pwhash = PasswordHashing()
app.secret_key="!@#"


@app.route("/userregister",methods=['POST'])
def userregister()->None:
    idno:str = request.form['idno']
    lastname:str = request.form['lastname']
    middlename:str = request.form['midinit']
    firstname:str = request.form['firstname']
    course:str = request.form['course']
    level:int = request.form['level']
    username:str = request.form['username']
    password:str = request.form['password']
    confirm_password:str = request.form['confirmpassword']
    if not idno or not lastname or not middlename or not firstname or not course or not level or not username or not password or not confirm_password:
        flash("Please fill all fields!", "warning")
        return render_template('register.html')

    if password != confirm_password:
        flash("Passwords do not match!", "warning")
        return render_template('register.html')

    flash("Registered successfully!", "info")
    #student = Student(idno=idno,lastname=lastname,firstname=firstname,midinit=middlename,course=course,level=level,password_plain=password)
    hashed_pw = pwhash.hashpassword(password)
    db.add_students(idno=idno,lastname=lastname,firstname=firstname,midinit=middlename,course=course,level=level,username=username,password_plain=password, password_hash=hashed_pw)
    return redirect(url_for('login'))


@app.route("/userlogin",methods=['POST'])
def userlogin()->None:
    username:str = request.form['username']
    password:str = request.form['password']
    students = db.getall_students()
    for student in students:
        if student['username'] == username and student['password_plain'] == password:
            flash("LOGIN SUCCESSFUL!")
            return redirect(url_for("landingpage"))
    flash("LOGIN FAILED!")
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
    return render_template("show.html",slist = db.getall_students(),pagetitle='student list', shownavbar=True)


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")