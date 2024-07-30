import dataclasses
import pickle
from datetime import datetime



@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(datas: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(datas, file)
    if datas:
        return max([len(data.students) for data in datas])
    return 0


def write_students_information(datas: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(datas, file)
    return len(datas)


def read_groups_information() -> list:

    with open("group.pickle", "rb") as file:
        datas = pickle.load(file)

    for data in datas:
        print("Data:", data)

    if datas:
        return list({data.specialty.name for data in datas})
    return []



def read_students_information() -> list:
    out = []
    with open("students.pickle", "rb") as file:
        datas = pickle.load(file)
    return datas










