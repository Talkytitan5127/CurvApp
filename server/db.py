from datetime import datetime

from flask import current_app

db = current_app.mysql


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    middle_name = db.Column(db.String(32))
    uuid = db.Column(db.String(128), nullable=False, unique=True)
    time_table = db.relationship('TimeTable', backref='employee', lazy=True)


class TimeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    is_exit = db.Column(db.Boolean, nullable=False, default=False)
    employee_id = db.Column(db.Integer, db.ForeignKey())
