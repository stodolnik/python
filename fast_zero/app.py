from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_rooot():
    return {'message': 'Hello World!'}
