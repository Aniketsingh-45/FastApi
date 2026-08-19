from fastapi import FastAPI
from schema.user_input import UserInput
from model.predict import predict_output, Model_version,model

from fastapi.responses import JSONResponse


app = FastAPI()


@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction API'}

@app.get('/health')
def health_check():
    return {'status':'healthy', 'Model_version':Model_version}

@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'region': data.region,
        'smoker': data.smoker 
    }

    try:
        premium = predict_output([user_input])

        return JSONResponse(status_code=200, content={'premium': premium})
 
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})