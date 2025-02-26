from pydantic import BaseModel, HttpUrl
from typing import Optional


class IterativeCrawlRequest(BaseModel):
    url: HttpUrl
    max_depth: Optional[int] = 3
    include_external: Optional[bool] = False
