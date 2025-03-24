from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) #Reference the app.py
from datetime import datetime

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./data.db"
#db is an instanc of SQL Alchemy class
db = SQLAlchemy(app)

#Create database Model
#Form class will inherit from Model class
class Form(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))
#decorator
@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["startDate"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]
        form = Form(first_name = first_name, last_name = last_name,
                email = email, date = date_obj, occupation = occupation)
        db.session.add(form)
        db.session.commit()
        #print(first_name, last_name, email, startDate, occupation)
    return render_template('index.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)