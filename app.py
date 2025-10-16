from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Form
from fastapi.templating import Jinja2Templates

app = FastAPI()  # 👈 this line is critical

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
def calculate(request: Request, stake: float = Form(...), odds: float = Form(...)):
    profit = round(stake * (odds - 1), 2)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "stake": stake, "odds": odds, "profit": profit}
    )
