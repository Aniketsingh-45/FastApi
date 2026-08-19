# pydantic model to validate incoming data
from pydantic import BaseModel, computed_field, Field
from typing import List, Dict, Optional, Literal, Annotated

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=18, lt=100, description='Enter the age of user')]
    bmi: Annotated[float, Field(..., gt=18, lt=100, description='Enter the bmi of user')]
    smoker: Annotated[str, Field(..., description='Enter the smoker status of user')]
    region: Annotated[str, Field(..., description='Enter the region of user')]

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker == "yes" and self.bmi > 30:
            return "high"
        elif self.smoker == "yes" and self.bmi > 27:
            return "medium"
        return "low"
 
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'young'
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return 'middle aged'
        return 'senior'