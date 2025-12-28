from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/health")
def health_check():
    return {
        "status": "alive",
        "service": "docflow",
    }

@app.get("/alive")
def is_alive():
    return {
        "alive": True,
    }

@app.get("/health_run")
def health_run():
    return {
        "no": "yes",
    }

@app.get("/")
def home():
    return {
        "home": True,
    }

@app.get("/echo")
def echo(msg: Optional[str] = None):
    return {
        "you_sent": msg,
    }