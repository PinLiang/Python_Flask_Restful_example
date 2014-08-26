import os
import time
from flask import Flask, request
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.sqlalchemy import SQLAlchemy
from threading import Thread
import simplejson as json
import random


parser = reqparse.RequestParser()
parser.add_argument('user', type=str)
print parser

app = Flask(__name__)
api = restful.Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/EV'
db = SQLAlchemy(app)

class IC(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    UN = db.Column(db.String(20), unique=True)
    PW = db.Column(db.String(20), unique=True)

class AB(db.Model):
    Riddle = db.Column(db.String(10), unique=True)
    ID = db.Column(db.Integer, primary_key=True)

class HelloWorld(restful.Resource):
    def post(self):
        a = IC.query.filter_by(ID = 0).first()
        b = AB.query.order_by(AB.ID.desc()).first()
        confirm = request.get_json(force = True)
        print confirm['name']
        print confirm['mystery']
        if((confirm['name'] != a.UN) or (confirm['mystery'] != a.PW)):
            return {"Response":"User name or Password Error!!!"}, 201
        else:
            return {"Mystery":b.Riddle}, 201

def get_random_word(wordLen):
    word = ''
    for i in range(wordLen):
        word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
    return word

def auto_change_key():
    #time.sleep(2678400)
    while True:
        b = AB.query.order_by(AB.ID.desc()).first()
        time.sleep(10)
        key = get_random_word(10)
        db.session.add(AB(Riddle=key,ID=b.ID+1))
        db.session.commit()


api.add_resource(HelloWorld, '/PinLiang/')
Thread(target = auto_change_key).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
