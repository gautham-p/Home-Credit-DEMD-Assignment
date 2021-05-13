import pandas as pd
import numpy as np
import pickle as pkl
from fastapi import FastAPI,Form,File,UploadFile
import uvicorn

app=FastAPI()

@app.get('/')
def base_route():
    return "Welcome to Home Credit"

@app.post('/creditcheck')
def credit(name1:str=Form(...),age:str=Form(...)):
    return f"{name1} {age}"

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=5000)