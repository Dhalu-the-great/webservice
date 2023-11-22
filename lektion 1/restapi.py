from fastapi import FastAPI
import uvicorn
from fastapi import responses
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/Static",StaticFiles(directory="lektion 1\Static"))

@app.get("/")
async def root():
    return {"version":"1.0"}

@app.get("/hallo")
async def root():
    return {"Hello":"World"}

@app.get("/bild")
async def bild():
    return  responses.FileResponse("Static/hund.jpg")

uvicorn.run(app,host="127.0.0.1", port=8000)