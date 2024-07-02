from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['DEBUG'] = True
socketio = SocketIO(app)

db = SQLAlchemy()
db.init_app(app)
"""
~$ python3
>>> from app import app, db
>>> with app.app_context():
...    db.create_all()
"""

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    src = db.Column(db.String(256))
    alt = db.Column(db.String(256))

    def __repr__(self):
        return '<Image %r>' % self.name

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)