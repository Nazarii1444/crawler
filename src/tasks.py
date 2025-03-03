import time
from celery import Celery

from src.config import REDIS_BACKEND, REDIS_BROKER
from src.sequential_crawler.crawler import crawl_website
from src.sequential_crawler.sitemap import generate_sitemap

app = Celery(
    "tasks",
    broker=REDIS_BROKER,
    backend=REDIS_BACKEND
)


@app.task
def run_sequential_crawler(url: str, depth: int, include_external: bool):
    start_time = time.time()
    site_structure = crawl_website(url, max_depth=depth, include_external=include_external)
    sitemap = generate_sitemap(site_structure)
    end_time = time.time()
    execution_time = end_time - start_time

    return {"sitemap": sitemap, "execution_time": execution_time}


@app.task(bind=True)
def run_threaded_crawler(url: str, depth: int, include_external: bool):
    return {1: 1}
