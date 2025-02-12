from fastapi import FastAPI

from stock.router import router as stock_router

app = FastAPI()
app.include_router(stock_router)

@app.get("/")
def root():
    return {"message": "Welcome to Project SAE AI Api Server!"}