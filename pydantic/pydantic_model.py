from pydantic import BaseModel
# type validation by pydantic
class Patient(BaseModel):
    name:str
    age:int


def insertpatient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")


patient_info= {"name":"Aniket", "age":30}
patient1=Patient(**patient_info)


insertpatient(patient1)




    
