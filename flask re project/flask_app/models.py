from typing import AsyncGenerator

from flask.globals import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Medicine(db.Model):
    __tablename__ = 'medicine'

    id = db.Column(db.Integer, primary_key=True)
    entpname = db.Column(db.String(22)) 
    itemname = db.Column(db.String(151))
    itemseq = db.Column(db.String(1000))
    efcyqesitm = db.Column(db.String(1000))
    usemethodqesitm = db.Column(db.String(1000))
    atpnwarnqesitm = db.Column(db.String(1000))
    atpnqesitm = db.Column(db.String(2000))
    intrcqesitm = db.Column(db.String(1000))
    seqesitm = db.Column(db.String(981))
    depositmethodqesitm = db.Column(db.String(157))
    opende = db.Column(db.Date)
    updatede = db.Column(db.Date)
    itemimage = db.Column(db.String(70))

    user_medicines = db.relationship("User_medicine", backref="medicine", cascade = 'all, delete')


class Users(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(32), db.Sequence('email_seq'), primary_key = True)
    password = db.Column(db.String(32))
    username = db.Column(db.String(32))
    age = db.Column(db.Integer)


class User_medicine(db.Model):
    __tablename__ = 'user_medicine'

    user_target_id = db.Column(db.Integer, primary_key = True)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'))
    user_itemname = db.Column(db.String(151))
    user_efcyqesitm = db.Column(db.String(1000))
    user_usemethodqesitm = db.Column(db.String(1000))


  
def get_medicinelist(search=None, check_query=None):
    if search is not None:
        search = f"%{search}%"
        if check_query == 1:
            return Medicine.query.filter(Medicine.entpname.like(search)).all()
        elif check_query == 2:
            return Medicine.query.filter(Medicine.itemname.like(search)).all()
        elif check_query == 3:
            return Medicine.query.filter(Medicine.efcyqesitm.like(search)).all()

    # return Medicine.query.all()


def get_um():
    
    return User_medicine.query.all()


def zero_to_none(data):
    if (data is None) or len(data) == 0:
        return None
    else:
        return data


