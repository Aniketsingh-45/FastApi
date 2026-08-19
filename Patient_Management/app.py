from pydantic import HttpUrl
from collections import defaultdict
from fastapi.openapi.utils import status_code_ranges
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,computed_field ,Field
from typing import Annotated,Literal,Optional

class Patient(BaseModel):

    id:Annotated[str,Field(...,description="Enter Patient ID: ",example="P001")]
    name:Annotated[str,Field(..., description='Enter the name', examples=["Aniket"])]
    age:Annotated[int, Field(...,gt=0,lt=120, description='enter the age of patient')]
    city:Annotated[str, Field(..., description='enter the city name ')]
    gender:Annotated[Literal['male','female','other'], Field(..., description='enter the gender of patient')]
    height:Annotated[float, Field(...,gt=1,lt=3, description='enter the height of patient in meters')]
    weight:Annotated[float, Field(...,gt=40,lt=150, description='enter the weight of patient in kgs')]


    @computed_field
    @property

    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property

    def verdict(self)->str:
        if self.bmi<18.5:
            return 'underweight'
        elif self.bmi<25:
            return 'normal'

        elif self.bmi<30:
            return 'overweight'
        
        else:
            return 'obese'

class PatientUpdate(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    gender:Annotated[Optional[Literal['male','female','other']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None)]
    weight:Annotated[Optional[float],Field(default=None)]



app=FastAPI() 

def load_data():
    with open('patient.json', 'r') as f:
        data=json.load(f)

    return data

def save_data(data):
    with open('patient.json','w')as f:
        json.dump(data,f)  


@app.get('/')
def hello():
    return{'message': 'Patient Management System Api'}

@app.get('/about')
def about():
    return {'message': 'A fully functional patient management system api'}


@app.get('/view')

def view():
    data=load_data()
    return data


@app.get('/patient/{patient_id}')

def view_patient(patient_id: str= Path(..., description="Enter Patient ID: ", example="P001")):

    data=load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail='Patient not found')
   
@app.get('/sort')

def sort_patient(sort_by: str =Query (..., description='sort on the basis of weight, height, bmi or age'), order: str = Query('asc', description='ascending or descending')):
    
    valid_sort=['height','weight','bmi']

    if sort_by not in valid_sort:
        raise HTTPException(status_code=404 , detail='Invalid sorting parameter{valid_sort}') 

    if order not in ['asc','desc']:
        raise HTTPException(status_code=404, detail="Invalid orderparameter{order}")

    data=load_data()

    sort_order=True if order=="asc" else False


    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.post('/create')

def create_patient(patient:Patient):

    #load data

    data=load_data()

    #check if patient already exists

    if patient.id in data:
        raise HTTPException(status_code=400 , detail=f'Patient {patient.id} already exists')

    #New patient add if not in data

    data[patient.id]=patient.model_dump(exclude=['id'])

    #save into json

    save_data(data)

    return JSONResponse(status_code=201, content={"message":"Patient created successfully"}) # 201 code for successfull work

@app.put('/edit/{patient_id}')

def update_patient(patient_id:str, patient_update:PatientUpdate ):

    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    existing_patient_info=data[patient_id]
    
    patient_update_info=patient_update.model_dump(exclude_unset=True)


    for key,value in patient_update_info.items():
        existing_patient_info[key]=value


    existing_patient_info['id']=patient_id
    patient_pydantic_obj=Patient(**existing_patient_info)

    existing_patient_info=patient_pydantic_obj.model_dump(exclude=['id'])

    data[patient_id]=existing_patient_info

    save_data(data)

    return JSONResponse(status_code=200, content={"message":"Patient updated successfully"})


@app.delete('/delete/{patient_id}')

def delete_patient(patient_id:str ):

    #load data
    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    #delete patient data

    del data[patient_id]

    #save data
    save_data(data)

    return JSONResponse(status_code=200,content={"message":"Patient deleted successfully"})
    
    





    
