from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_list = db.Column(db.String(200), index =True)


class TodoForm(FlaskForm):
    todo = StringField('New Todo')
    submit = SubmitField('Add')

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():

    if 'todo' in request.form:
        db.seesion.add(Todo(todo_list=request.form['todo']))
        db.session.commit()
    return render_template('index.html', todos=Todo.query.all(), template_form=TodoForm())



