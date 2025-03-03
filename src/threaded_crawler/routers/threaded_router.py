from fastapi import APIRouter
from src.tasks import run_threaded_crawler, app as celery_app

threaded_router = APIRouter()


@threaded_router.post("/crawl/threaded")
def threaded_crawl(request):
    return {1: 1}


@threaded_router.get("/crawl/status/{task_id}")
def get_task_status(task_id: str):
    task_result = celery_app.AsyncResult(task_id)

    start_time = task_result.info.get("start_time") if task_result.info else None
    execution_time = task_result.info.get("execution_time") if task_result.ready() else None

    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None,
        "start_time": start_time,
        "execution_time": execution_time
    }
