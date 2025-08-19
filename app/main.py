from fastapi import FastAPI
from app.routes import routes

app = FastAPI(title="Quantum Portfolio Optimizer API")

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "Quantum Portfolio Optimizer API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1.", port=8000)