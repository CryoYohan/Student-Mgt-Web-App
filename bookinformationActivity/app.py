from flask import Flask,render_template,request,url_for,redirect,flash, session
from dbhelper import Databasehelper

app = Flask(__name__)
db = Databasehelper()
app.secret_key="!@#"

booktable = 'books'

bookcolumns:list = ['isbn', 'title', 'author', 'copyright', 'edition', 'price', 'qty', 'total', 'action']

@app.route('/cancel')
def cancel():
    flash("Adding Book Cancelled!", "error")
    return redirect(url_for('books'))

@app.route("/updatebook/<isbn>", methods=["POST"])
def updatebook(isbn):
    title:str = request.form['title']
    author:str = request.form['author']
    copyright:str = request.form['copyright']
    edition:str = request.form['edition']
    try:
        price:float = request.form['price']
        quantity:int = request.form['qty']
        total:float = int(quantity) * float(price)
        db.update_record(table=booktable,isbn=isbn,title=title,author=author,copyright=copyright,edition=edition,price=price,qty=quantity,total=total)
        flash("Book Updated Successfully!", "info")
        return redirect(url_for('books'))
    except ValueError:
        flash(f"Error: Invalid Input!", 'error')
        return redirect(url_for('books'))

@app.route('/deletebook/<student_idno>')
def deletebook(student_idno):
    db.delete_record(table=booktable,isbn=student_idno)
    flash('Book Deleted Successfully!', 'info')
    return redirect(url_for('books'))

@app.route("/addbook", methods=['POST'])
def addbook():
    price:float = 0.00
    quantity:int = 0
    total:float = 0.00
    isbn:str = ''

    isbn = request.form['isbn']
    title = request.form['title']
    author = request.form['author']
    copyright = request.form['copyright']
    edition = request.form['edition']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    total = quantity * price
    if not idno_duplicate(table=booktable, isbn=isbn):
        db.add_record(table=booktable, isbn=isbn, title=title, author=author, copyright=copyright,
                    edition=edition, price=price, qty=quantity, total=total)
        flash("Book Added Successfully!", 'info')
    else:
        flash("Error! Book not added", 'error')

    return redirect(url_for('books'))
 
    


def idno_duplicate(table,**args)->bool:
    records = db.getall_records(table=table)
    for record in records:
        if record['isbn'] == args.get('isbn'):
                flash("ISBN already exist!", "error")
                return True
    return False
         
               
@app.route("/")
def books()->None:
    return render_template("books.html",booklist = db.getall_records(table=booktable),bookcolumns=bookcolumns,bartitle='Book Information')


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=2003)