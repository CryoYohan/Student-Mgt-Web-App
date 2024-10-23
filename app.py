from flask import Flask,render_template,request,url_for,redirect,flash, session
from dbhelper import Databasehelper
from student import Student
from hashpw import PasswordHashing
from time import sleep

app = Flask(__name__)
db = Databasehelper()
pwhash = PasswordHashing()
app.secret_key="!@#"



@app.route("/addstudent", methods=['POST'])
def addstudent():
    idno:str = request.form['idno']
    lastname:str = request.form['lastname']
    middlename:str = request.form['midinit']
    firstname:str = request.form['firstname']
    course:str = request.form['course']
    level:int = request.form['level']
    username:str = f"tu-{idno}"
    password:str = f"{idno}-{lastname[0]}"
    if not idno_duplicate(idno,username):
        hashed_pw = pwhash.hashpassword(password)
        student = Student(idno=idno,lastname=lastname,firstname=firstname,midinit=middlename,course=course,level=level,username=username,password_plain=password, password_hash=hashed_pw)
        db.add_students(**student.__dict__)
        flash("Student Added Successfully!", "info")
        return redirect( url_for('show') )

    else:
        flash("Error! Student not Added", "error")
        return redirect( url_for('show') )


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

    if not idno_duplicate(idno,username):
        hashed_pw = pwhash.hashpassword(password)
        student = Student(idno=idno,lastname=lastname,firstname=firstname,midinit=middlename,course=course,level=level,username=username,password_plain=password, password_hash=hashed_pw)
        db.add_students(**student.__dict__)
        flash("Registered successfully!", "info")
        return redirect(url_for('login'))
    else:
        return redirect(url_for('register'))



def idno_duplicate(idno:str, username:str)->bool:
    students = db.getall_students()
    for student in students:
        if student['idno'] == idno:
            flash("User ID already exist!", "warning")
            return True
        
        if student['username'] == username:
            flash("Username already exist!", "warning")
            return True
    return False

@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache,no-store,must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route("/logout")
def logout():
    session['name'] = None
    return redirect(url_for("login"))

@app.route('/updatestudent')
def updatestudent():
    return redirect(url_for('login')) if not session.get('name') else render_template("updatestudent.html", pagetitle="Update Student Information", shownavbar=True)

@app.route("/userlogin",methods=['POST'])
def userlogin()->None:
    username:str = request.form['username']
    password:str = request.form['password']
    students = db.getall_students()
    for student in students:
        if student['username'] == username and student['password_plain'] == password:
            flash("LOGIN SUCCESSFUL!")
            session['name'] = username
            return redirect(url_for("index"))
    flash("LOGIN FAILED!")
    return redirect(url_for("login"))
            
               
@app.route("/register")
def register():
    return render_template("register.html", pagetitle="Register",shownavbar=False)


@app.route("/login")
def login()->None:
    return render_template("login.html",pagetitle='user login',shownavbar=False)

@app.route("/showstudents")
def show()->None:
    return redirect("login") if not session.get("name") else render_template("show.html",slist = db.getall_students(),pagetitle='student list', shownavbar=True)


@app.route("/")
def index():
    return redirect(url_for('login')) if not session.get('name') else render_template("index.html",pagetitle='Tidert\'s University',shownavbar=True)


@app.route("/landingpage")
def landingpage():
    return redirect("login") if not session.get("name") else render_template("landingpage.html",pagetitle='Tidert\'s University',shownavbar=True)

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")