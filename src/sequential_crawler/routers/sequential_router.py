from fastapi import APIRouter

from src.sequential_crawler.crawler import crawl_website
from src.sequential_crawler.sitemap import generate_sitemap
from src.sequential_crawler.models import IterativeCrawlRequest
from src.logger import logger


sequential_router = APIRouter()

@sequential_router.post("/crawl/iterative")
def iterative_crawl(request: IterativeCrawlRequest):
    url_str = str(request.url)
    max_depth = request.max_depth
    include_external = request.include_external

    # logger.debug(str(url_str) + str(max_depth) + str(include_external))
    urls = crawl_website(url_str, max_depth, include_external=include_external)
    sitemap = generate_sitemap(urls)
    return {"sitemap": sitemap}
