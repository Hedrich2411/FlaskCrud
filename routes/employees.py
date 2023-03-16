from flask import Blueprint, render_template, request, redirect, url_for
from models.employee import Employee
from utils.db import db

employees = Blueprint("employees", __name__)


@employees.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@employees.route('/new', methods=['POST'])
def add_employee():
    if request.method == 'POST':

        name = request.form['name']
        lastname = request.form['lastname']
        identification = request.form['identification']
        email = request.form['email']

        new_employee = Employee(name, lastname, identification, email)

        db.session.add(new_employee)
        db.session.commit()

        return redirect(url_for('employees.index'))


@employees.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    employee = Employee.query.get(id)

    if request.method == "POST":
        employee.name = request.form['name']
        employee.lastname = request.form['lastname']
        employee.identification = request.form['identification']
        employee.email = request.form['email']

        db.session.commit()

        return redirect(url_for('employees.index'))

    return render_template("update.html", employee=employee)


@employees.route("/delete/<id>", methods=["GET"])
def delete(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for('employees.index'))


