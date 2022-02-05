
from datetime import datetime
from turtle import title
from flask import Flask, redirect, render_template, request  # creating Flask Instance
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import desc
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TODO.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class dataoftodo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

@app.route("/")  # sending same function on both routes
@app.route("/home")  # Routes
def home_page():
    data = dataoftodo.query.all()
    return render_template('home.html', data=data)

@app.route("/submit", methods=['GET', 'POST'])
def submitform():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['descinform']
        data = dataoftodo(title=title, desc=desc)
        db.session.add(data)
        db.session.commit()
    return redirect('/home')

@app.route('/delete/<id>')
def delete(id):
    recordtodelete = dataoftodo.query.get_or_404(id)

    try:
        db.session.delete(recordtodelete)
        db.session.commit()
        return redirect('/home')
    except:
        return "Some Error Occurred, Try Again or Report the error"

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    recordtoupdate = dataoftodo.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['descinform']
        recordtoupdate.title = title
        recordtoupdate.desc = desc
        try:
            db.session.commit()
            return redirect('/home')
        except:
            return "Some Error Occurred, Try Again or Report the error"

    else:
        return render_template('update.html',recordtoupdate=recordtoupdate)

if __name__ == "__main__":
    app.run(debug=True, port=80)