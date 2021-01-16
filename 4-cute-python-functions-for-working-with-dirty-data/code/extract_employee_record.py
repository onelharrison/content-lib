import time
from dataclasses import dataclass
from typing import Optional

from safe_cast import safe_cast


@dataclass
class Employee:
    name: str
    age: Optional[int] = None
    job_title: str
    updated_at: int


def extract_employee_record(employee_data):
    employee = Employee()
    employee.name = employee_data["name"]
    employee.age = safe_cast(employee_data["age"], int)
    employee.job_title = employee_data["job_title"]
    employee.updated_at = int(time.time())
    return employee


employee_tamara = {
    "name": "Tamara Rivers",
    "age": "",  # age is missing from the source system
    "job_title": "Director of Engineering",
}

tamara = extract_employee_record(employee_tamara)
print(tamara.age)  # None

employee_bianca = {
    "name": "Bianca Brown",
    "age": "39",
    "job_title": "Chief Technology Officer",
}

bianca = extract_employee_record(employee_bianca)
print(bianca.age)  # 39
