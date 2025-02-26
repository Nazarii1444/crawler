from celery import Celery
from src.sequential_crawler.crawler import crawl_website
from src.sequential_crawler.sitemap import generate_sitemap


app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)


@app.task
def run_crawler(url: str, depth: int = 2):
    site_structure = crawl_website(url, max_depth=depth)
    return generate_sitemap(site_structure)
