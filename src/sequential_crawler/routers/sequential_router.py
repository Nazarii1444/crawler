from fastapi import APIRouter
from src.sequential_crawler.models import IterativeCrawlRequest
from src.tasks import run_sequential_crawler, app as celery_app

sequential_router = APIRouter()


@sequential_router.post("/crawl/iterative")
def iterative_crawl(request: IterativeCrawlRequest):
    url_str = str(request.url)
    max_depth = request.max_depth
    include_external = request.include_external

    task = run_sequential_crawler.apply_async(args=[url_str, max_depth, include_external])
    return {"task_id": task.id, "status": "Processing"}


@sequential_router.get("/crawl/status/{task_id}")
def get_task_status(task_id: str):
    task_result = celery_app.AsyncResult(task_id)

    sitemap = task_result.result.get("sitemap") if task_result.ready() else None
    execution_time = task_result.info.get("execution_time") if task_result.ready() else None

    return {
        "task_id": task_id,
        "status": task_result.status,
        "sitemap": sitemap,
        "execution_time": execution_time
    }
