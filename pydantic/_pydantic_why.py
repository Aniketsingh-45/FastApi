# what is pydantic
# pydantic is a data validation library for python

# why we need pydantic
#  we need pydantic to validate the data coming from the user
# it ensure the data is of the correct type
# it also ensure the data is of the correct format
#it also ensure the data is of the correct value
#it also ensure the data is of the correct range

#for add
def insert_patient_data(name:str, age:int):
    if type(name)== str and type(age)==int:
        print(name)
        print(age)
        print("insertd into database")

    else:
        raise TypeError('invalid data types')

insert_patient_data('bhuvan',42)


#For update


def update_patient_data(name:str, age:int):

  
    if type(name)== str and type(age)==int:
        if age< 0:
            raise ValueError("Age cannot be negative")
        else:
            print(name)
            print(age)
            print("Updated the data")

    else:
        raise TypeError('invalid data types')

update_patient_data('bhuvan',42)
