import time

# import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.config import allowed_origins
from src.sequential_crawler.routers.sequential_router import sequential_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(sequential_router, prefix="/api/sequential", tags=["Admin"])

# if __name__ == '__main__':
#     uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)
