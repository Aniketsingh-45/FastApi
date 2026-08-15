from fastapi import FastAPI


app=FastAPI()

@app.get('/')
def hello ():
    return {'message': 'Hello World'}

@app.get('/about')
def about():
    return {'message': 'My name is Aniket Singh and I am a developer'}