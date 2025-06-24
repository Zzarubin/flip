from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Путь до фронтенда
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

# Отдача index.html по корню
@app.get("/")
async def root():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

# Статика (если будут CSS/JS)
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
