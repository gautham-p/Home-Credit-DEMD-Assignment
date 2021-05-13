import pandas as pd
import numpy as np
import pickle as pkl
from fastapi import FastAPI,Form,File,UploadFile
import uvicorn
from sklearn.preprocessing import StandardScaler
import os

app=FastAPI()
scaler = StandardScaler()

#Loading Pickle File
pick=open("Home_Credit_Model.pkl","rb")
model=pkl.load(pick)
pick.close()

@app.get('/')
def base_route():
    return "Welcome to Home Credit"

@app.post('/creditcheck')
def credit(city:int=Form(...),ext1:float=Form(...),ext2:float=Form(...),ext3:float=Form(...),circle:int=Form(...),doc3:int=Form(...),contract:int=Form(...),gender:int=Form(...),car:int=Form(...),edu:int=Form(...)):
    result=model.predict([[city,ext1,ext2,ext3,circle,doc3,contract,gender,car,edu]])#Values of 16th row in test.csv in data folder
    if result in [0,"0"]:return "Loan Denied"
    return "Loan Approved"

@app.post('/bulkcreditcheck')
def bulkcredit(file1:UploadFile=File(...)):
    df=pd.read_csv(file1.file,index_col ='SK_ID_CURR') #Loading test.csv file in data folder
    result=model.predict(df)
    return f"The results for {file1.filename} are {result}"

if __name__ == "__main__":
    if os.environ['ENVIRONMENT']=="production":
        pt=int(os.environ.get('PORT',5000))
        uvicorn.run(app,host="0.0.0.0",port=pt)
    else:
        uvicorn.run(app,host="0.0.0.0",port=5000)