import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

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
    return {"message": "Hello, Render! Your FastAPI service is running."}

@app.get("/api")
def api():
    return {"status": "success", "data": "This is a Render Web Service!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # 取得 Render 設定的 PORT，預設 8000
    print(f"🚀 Server is running on http://0.0.0.0:{port}")  # 終端機顯示啟動訊息
    uvicorn.run(app, host="0.0.0.0", port=port)
