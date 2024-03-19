from fastapi import FastAPI, BackgroundTasks, HTTPException, Query
from pydantic import BaseModel
from extract import *
import os


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
async def get_homepage_data(wallet: str = Query(...)):
  #  print(wallet)
 #   wallet_main = wallet.split("::")[0]
 #   print(wallet_main)
 #   url = wallet.split("::")[1]
    data = get_reward("tgWebAppData=query_id%3DAAGiuD5zAAAAAKK4PnM04zI4%26user%3D%257B%2522id%2522%253A1933490338%252C%2522first_name%2522%253A%2522Lakshay%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Lakshay0101%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1710837904%26hash%3D33c8db1983ea4951583175a780610df5ab028ce846831523e20cfb90e2b68e2c","code onion old dream teach play main science flame final depend question")
    return data



@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    

