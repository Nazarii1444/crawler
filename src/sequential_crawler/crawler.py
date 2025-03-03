import re
from typing import List, Tuple, Dict
from urllib.parse import urljoin, urlparse

import httpx

from src.config import logger

def extract_links(url: str) -> Tuple[List[str], List[str]]:
    try:
        response = httpx.get(url, timeout=5)
        response.raise_for_status()

        html = response.text
        links = set(re.findall(r'href=["\'](.*?)["\']', html))
        base_domain = urlparse(url).netloc

        internal_links, external_links = set(), set()

        for link in links:
            absolute_link = urljoin(url, link)
            parsed_link = urlparse(absolute_link).netloc

            if parsed_link == base_domain:
                internal_links.add(absolute_link)
            else:
                external_links.add(absolute_link)

        return list(internal_links), list(external_links)
    except Exception as e:
        logger.error(f"Помилка при завантаженні {url}: {e}")
        return [], []


def crawl_website(start_url: str, visited=None, max_depth: int = 3, include_external=False) -> Dict[str, str] | None:
    if visited is None:
        visited = set()

    if start_url in visited or max_depth == 0:
        return None

    visited.add(start_url)
    internal_links, external_links = extract_links(start_url)

    node = {
        "url": start_url,
        "internal": [],
        "external": external_links
    }

    if include_external:
        node["external"] = external_links

    for link in internal_links:
        if link not in visited:
            child_node = crawl_website(link, visited=visited, max_depth=max_depth - 1, include_external=include_external)
            if child_node:
                node["internal"].append(child_node)

    return node
