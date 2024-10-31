from flask import Flask,render_template,request,url_for,redirect,flash, session
from dbhelper import Databasehelper
from student import Student
from hashpw import PasswordHashing
from time import sleep

app = Flask(__name__)
db = Databasehelper()
pwhash = PasswordHashing()
app.secret_key="!@#"

studtable = "students"
booktable = "books"

bookcolumns:list = ['isbn', 'title', 'author', 'copyright', 'edition', 'price', 'qty', 'total', 'action']


@app.route("/account")
def account():
    return redirect(url_for('login')) if not session.get('name') else render_template("account.html", pagetitle="Account Information", shownavbar=True)

@app.route('/deletestudent/<student_idno>')
def deletestudent(student_idno):
    db.delete_record(table=studtable,idno=student_idno)
    flash('Student Deleted Successfully!', 'info')
    return redirect(url_for('show'))


@app.route("/updatestudent", methods=["POST"])
def updatestudent():
    lastname = request.form['lastname']
    middlename = request.form['midinit']
    firstname = request.form['firstname']
    course = request.form['course']
    level = request.form['level']
    db.update_recordd(table=studtable,lastname=lastname, midinit=middlename, firstname=firstname, course=course, level=level)
    flash("Student Updated Successfully!", "info")
    return redirect(url_for('show'))

@app.route("/addbook", methods=['POST'])
def addbook():
    isbn:str = request.form['isbn']
    title:str = request.form['title']
    author:str = request.form['author']
    copyright:str = request.form['copyright']
    edition:str = request.form['edition']
    price:float = request.form['price']
    quantity:int = request.form['quantity']
    total:float = quantity * price
    if not idno_duplicate(table=booktable,idno=isbn):
        db.add_record(table=booktable, isbn=isbn,title=title,author=author,copyright=copyright,edition=edition,price=price,quantity=quantity,total=total)
        flash("Book Added Succesfully!", 'info')
    else:
        flash("Error! Book not added", 'error')
    
@app.route("/addstudent", methods=['POST'])
def addstudent():
    idno:str = request.form['idno']
    lastname:str = request.form['lastname']
    middlename:str = request.form['midinit']
    firstname:str = request.form['firstname']
    course:str = request.form['course']
    level:int = request.form['level']
    username:str = f"tu-{idno}"
    password:str = f"{idno}-{lastname[0].lower()}"
    if not idno_duplicate(table=studtable,idno=idno,username=username):
        hashed_pw = pwhash.hashpassword(password)
        student = Student(idno=idno,lastname=lastname,firstname=firstname,midinit=middlename,course=course,level=level,username=username,password_plain=password, password_hash=hashed_pw)
        db.add_record(table=studtable,**student.__dict__)
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

    if password != confirm_password:
        flash("Passwords do not match!", "error")
        return render_template('register.html')

    if not idno_duplicate(table=studtable,idno=idno,username=username):
        hashed_pw = pwhash.hashpassword(password)
        student = Student(idno=idno,lastname=lastname,firstname=firstname,midinit=middlename,course=course,level=level,username=username,password_plain=password, password_hash=hashed_pw)
        db.add_record(table=studtable,**student.__dict__)
        flash("Registered successfully!", "info")
        return redirect(url_for('login'))



def idno_duplicate(table,**args)->bool:
    records = db.getall_records(table=table)
    if table == 'students':
        for record in records:
            if record['idno'] == args.get('idno'):
                flash("User ID already exist!", "error")
                return True
            
            if record['username'] == args.get('username'):
                flash("Username already exist!", "error")
                return True
    else:
        for record in records:
            if record['isbn'] == args.get('isbn'):
                    flash("ISBN already exist!", "error")
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


@app.route("/userlogin",methods=['POST'])
def userlogin()->None:
    username:str = request.form['username']
    password:str = request.form['password']
    students = db.getall_records(table=studtable)
    for student in students:
        if student['username'] == username and student['password_plain'] == password:
            flash("LOGIN SUCCESSFUL!", "info")
            session['name'] = username
            return redirect(url_for("index"))
    flash("LOGIN FAILED!", "error")
    return redirect(url_for("login"))
            
               
@app.route("/register")
def register():
    return render_template("register.html", pagetitle="Register",shownavbar=False)


@app.route("/login")
def login()->None:
    return render_template("login.html",pagetitle='user login',shownavbar=False)

@app.route("/books")
def books()->None:
    return redirect("login") if not session.get("name") else render_template("books.html",booklist = db.getall_records(table=booktable),bookcolumns=bookcolumns,pagetitle='Manage Books', shownavbar=True)

@app.route("/showstudents")
def show()->None:
    return redirect("login") if not session.get("name") else render_template("show.html",slist = db.getall_records(table=studtable),pagetitle='student list', shownavbar=True)


@app.route("/")
def index():
    return redirect(url_for('login')) if not session.get('name') else render_template("index.html",pagetitle='Tidert\'s University',shownavbar=True)


@app.route("/landingpage")
def landingpage():
    return redirect("login") if not session.get("name") else render_template("landingpage.html",pagetitle='Tidert\'s University',shownavbar=True)

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")