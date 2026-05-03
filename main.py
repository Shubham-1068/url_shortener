from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import random
import string
import os
from configuration import collection
from database.schema import short_url, response_parser
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

load_dotenv()

val = ""
val += string.ascii_letters
val += string.digits

app = FastAPI()
templates = Jinja2Templates(directory="views")

# Get base URL from environment or use localhost for development
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})


@app.get("/shorturl")
def get_shortened_url(req: str):
    res = ""

    data = collection.find()
    data = response_parser(data)

    for i in data:
        if i["lurl"] == req:
            return JSONResponse({
                "message" : "Short URL already exists"
            })

    for _ in range(random.randint(3,8)):
        res += random.choice(val)

    collection.insert_one(short_url({
        "surl" : res,
        "lurl" : req
    }))

    return JSONResponse({
        "message" : "Short URL created",
        "New URL" : f"{BASE_URL}/{res}"
    })
    

@app.get("/{req}")
def get_full_url(req: str):

    data = collection.find()
    data = response_parser(data)

    for i in data:
        if i["surl"]==req:
            return RedirectResponse(i["lurl"])
        
    return JSONResponse({
        "message" : "No such URL found"
    })
