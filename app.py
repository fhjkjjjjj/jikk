from fastapi import FastAPI, BackgroundTasks, HTTPException, Query
from pydantic import BaseModel
from extract import *
import os
import base64

SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage
@app.get("/test")
async def get_homepage_data(wallet: str = Query(...),data: str = Query(...)):
    print(wallet)
    print(data) 
    data = download() 
    return data



@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    

