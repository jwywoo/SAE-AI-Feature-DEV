from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Updated to 'routes.py' if renamed
from stock.router import router as stock_router
from config import get_settings

app = FastAPI(title="SAE AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include stock router
app.include_router(stock_router)


@app.get("/")
def root():
    return {"message": "Welcome to Project SAE AI API Server!"}
