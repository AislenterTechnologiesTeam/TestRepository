
from datetime import datetime
from run import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    adhar = db.Column(db.Integer)
    dob = db.Column(db.Integer)
    mobile = db.Column(db.Integer)
    policy_name = db.Column(db.String(50))
    amount = db.Column(db.Integer)
    policydate = db.Column(db.DateTime, default=datetime.utcnow)
    policyduration =db.Column(db.DateTime)
    agencycode = db.Column(db.Integer,)
    gender = db.Column(db.String(20))
    address = db.Column(db.VARCHAR)

   
class Agent(db.Model):
    agent_name = db.Column(db.String(50))
    agent_id = db.Column(db.Integer, primary_key=True)
    no_of_policy = db.Column(db.Integer)
    email_id = db.Column(db.VARCHAR(50))
    mobile = db.Column(db.Integer)
    address = db.Column(db.VARCHAR)
    qualification =db.Column(db.VARCHAR)
    agency_date = db.Column(db.DateTime, default=datetime.utcnow)
    group_name = db.Column(db.VARCHAR(120))
    image = db.Column(db.LargeBinary)


class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_name = db.Column(db.VARCHAR)
    policy_year = db.Column(db.Integer)


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    time = db.Column(db.VARCHAR)


class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competition_date = db.Column(db.DateTime)
    expiry_year = db.Column(db.DateTime)
    no_of_policy = db.Column(db.Integer)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_nanme = db.Column(db.VARCHAR)    