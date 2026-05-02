from app import db
from datetime import datetime

class Employment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    employee_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    position = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

    hire_date = db.Column(db.Date, default=datetime.utcnow)
    salary = db.Column(db.Float, nullable=False)

    status = db.Column(db.String(20), default="active")  # active / inactive

    def __repr__(self):
        return f"<Employment {self.employee_name}>"