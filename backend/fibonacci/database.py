from flask_sqlalchemy import SQLAlchemy
from typing import List, Tuple
from datetime import date, datetime

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

def get_value_on_index(index: int):
    return FibonacciRecord.query.filter_by(index=index).first()

def add_or_update_fibonacci_record(index, value):
    record = get_value_on_index(index)
    if record is None:
        record = FibonacciRecord(index=index, value=value, date_calculated=datetime.now())
        db.session.add(record)
        db.session.commit()
    else:
        record.date_calculated = datetime.now()
        db.session.commit()
    
def get_last_n_records(amount: int):
    return FibonacciRecord.query.order_by(FibonacciRecord.date_calculated.desc()).limit(amount).all()

class FibonacciRecord(db.Model):
    index = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    date_calculated = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f'fibonacci({self.index}) = {self.value} (calculated @ {self.date_calculated})'