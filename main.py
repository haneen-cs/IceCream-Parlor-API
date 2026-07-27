from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from icecreams import router

app=FastAPI()

# 1. Mount the "static" folder so FastAPI can read static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Include your icecream routes (unchanged)
app.include_router(router)

# 3. Serve index.html when you open http://127.0.0.1:8000/
@app.get("/")
def test():
    return FileResponse("static/index.html")

app.include_router(router)
@app.get("/",description="first end point")
def test():
    return {
        "message":"first endpoint .... "
    }
