from fastapi import FastAPI
from pora import students

app = FastAPI()  # creating a app object


@app.get("/")
def show_wecome():
    return "hello world,welcome to fastapi"


@app.get("/mobiles")
def mobile():
    return "fav mob z7pro"


# @app.get("/{id}")
# def get_id(id:int):
#     return {"MSG":f"valid not found {id}"}


@app.get("/{id}")
def get_data(id:int):
    for fri in students:
        if fri.get("id") == id:
            return fri
    return {"msg": f"no friends id {id}"}





#main.py-> for the logic point and entry point for the app
#schemas.py-> to define structure of thr from user


#db.py->