from flask import render_template, request, redirect, url_for
from . import employment_bp
from app import db
from .models import Employment

# READ - List employees
@employment_bp.route("/")
def index():
    employees = Employment.query.all()
    return render_template("employment/index.html", employees=employees)


# CREATE
@employment_bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        emp = Employment(
            employee_name=request.form["name"],
            email=request.form["email"],
            position=request.form["position"],
            department=request.form["department"],
            salary=request.form["salary"]
        )
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for("employment.index"))

    return render_template("employment/add.html")