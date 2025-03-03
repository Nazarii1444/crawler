import uvicorn
from fastapi import FastAPI

from src.middlewares import setup_middlewares
from src.sequential_crawler.routers.sequential_router import sequential_router

app = FastAPI()
setup_middlewares(app)

app.include_router(sequential_router, prefix="/api/sequential", tags=["Admin"])

if __name__ == '__main__':
    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)
