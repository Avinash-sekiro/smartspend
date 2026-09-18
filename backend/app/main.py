from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def server_health():
    return {"status": "healthy"}