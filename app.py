from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import cv2, base64, json

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

def img2json(img):
    img_data = cv2.imencode('.jpg', img)[1]
    json_string = json.dumps({"image": base64.b64encode(img_data).decode('utf-8')})
    return json_string

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    src = db.Column(db.String(256))
    alt = db.Column(db.String(256))

    def __repr__(self):
        return '<Image %r>' % self.name

@socketio.on("update")
def update_image():
    socketio.emit("server originated", {"image": "Nothing"})

@app.route("/")
def index():
    img = cv2.imread('static/Magazine.jpg')
    json_img = img2json(img)
    socketio.emit("server originated", {"image": "Nothing"})
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)