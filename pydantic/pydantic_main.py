from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List, Dict, Optional,Annotated
# data validation by pydantic
#Field-metadata
#Annotated-to apply metadata on the field

class Patient(BaseModel):
    name:str=Annotated[str, Field(max_length=50, title="Name of the patient", description="write name under 50 character", examples=['aniket', 'bhuvan','yash'] )]
    email:EmailStr #email validation
    linkedin:AnyUrl #url validation
    age:int 
    weight:Annotated[float, Field(gt=0, lt=100, strict=True)] #weight between 0 and 100 and must be float
    married:bool
    allergies: Optional[List[str]]=None
    contact_detail:Dict[str, str]
  

def insertpatient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkedin)
    print("inserted")



def updatepatient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.email)
    print(patient.linkedin)
    print(patient.weight)
    print("updated") 


patient_info= {"name":"Aniket","email":"abc@gmail.com","linkedin":"https://www.linkedin.com/in/aniket-shinde-a1b2c3d4e5f6/", "age":30, "weight":12.5, "married":True, "allergies":["penicillin", "latex"], "contact_detail":{"phone":"1234567890"}}
patient1=Patient(**patient_info)


updatepatient(patient1) 




    
