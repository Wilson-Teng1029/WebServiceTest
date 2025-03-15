from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允許 CORS，讓前端可以請求 API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello, Render!"}

@app.get("/api")
def api():
    return {"status": "success", "data": "This is a Render Web Service!"}
