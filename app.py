from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

import traceback

@app.middleware("http")
async def log_exceptions(request, call_next):
    try:
        return await call_next(request)
    except Exception:
        traceback.print_exc()   # <- prints full stacktrace to Railway logs
        raise                   # let FastAPI still return 500


# serve /static (css, logos, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/calculator", response_class=HTMLResponse)
async def calculator(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})

@app.get("/faqs", response_class=HTMLResponse)
async def faqs(request: Request):
    return templates.TemplateResponse("faqs.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
