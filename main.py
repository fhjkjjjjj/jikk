from flask import Flask, request
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return "hello"

if __name__ == "__main__":
    app.run(debug=True)
