from fastapi import FastAPI

app=FastAPI()

sports_team={
    1: {"name":"vk",
       "age":22,
       "event":"vollyball"
       }

}

@app.get("/name")
def sports():
    return {"name":"akhila"}

@app.get("/get_team/{player_no}")
def sports_name(player_no:int):
        return sports_team[player_no]

@app.get("/get_name")
def get_team(name:str):
    for player_no in sports_team:
        if sports_team[player_no]["name"]==name:
            return sports_team[player_no]
        return{"data":"no"}

