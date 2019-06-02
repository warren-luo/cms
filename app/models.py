# coding:utf8
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

# Instance Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]        = "mysql+pymysql://wluo@wasuwikisvr:Bgq_StJwpoCkzqot2gV9@wasuwikisvr.mysql.database.chinacloudapi.cn:3306/wasuwiki"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Instance SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id       = db.Column(db.Integer,  primary_key=True)
    username = db.Column(db.String(20),  nullable=False)
    password = db.Column(db.String(100), nullable=False)
    addtime  = db.Column(db.DateTime,    nullable=False, default=datetime.now)

if __name__ == "__main__":
    db.create_all()