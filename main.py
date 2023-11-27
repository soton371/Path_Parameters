import json
from fastapi import FastAPI, Path
from models import Employee
from mongoengine import connect

app = FastAPI()
connect(db="hrms", host="localhost", port=27017)


@app.get('/')
def path_para():
    return {"msg": "path parameter"}


@app.get('/get_all_employees')
def get_all_employees():
    employees = json.loads(Employee.objects().to_json())
    return {"employees": employees}


@app.get('/get_employee/{emp_id}')
def get_employee(emp_id: int = Path(..., gt=0)):
    employee = Employee.objects.get(emp_id=emp_id)

    # specific information
    employee_dict = {
        "emp_id": employee.emp_id,
        "name": employee.name,
        "age": employee.age,
        "teams": employee.teams
    }

    # employee all information
    tt = json.loads(employee.to_json())

    return tt
