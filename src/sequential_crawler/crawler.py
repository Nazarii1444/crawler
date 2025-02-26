import re
from typing import List, Tuple, Dict
from urllib.parse import urljoin, urlparse

import httpx

from src.logger import logger

def extract_links(url: str) -> Tuple[List[str], List[str]]:
    try:
        response = httpx.get(url, timeout=5)
        response.raise_for_status()

        html = response.text
        links = set(re.findall(r'href=["\'](.*?)["\']', html))
        # logger.debug("===== LINKS =====")
        # logger.debug(links)
        base_domain = urlparse(url).netloc

        internal_links, external_links = set(), set()

        for link in links:
            absolute_link = urljoin(url, link)
            # logger.debug("ABS: " + absolute_link)
            parsed_link = urlparse(absolute_link).netloc
            # logger.debug("PRS: " + parsed_link)

            if parsed_link == base_domain:
                internal_links.add(absolute_link)
            else:
                external_links.add(absolute_link)

        return list(internal_links), list(external_links)
    except Exception as e:
        logger.error(f"Помилка при завантаженні {url}: {e}")
        return [], []


def crawl_website(start_url: str, max_depth: int = 3, visited=None, include_external=False) -> Dict[str, str] | None:
    """Рекурсивний обхід сайту для побудови вкладеної структури"""
    if visited is None:
        visited = set()

    if start_url in visited or max_depth == 0:
        return None

    visited.add(start_url)
    internal_links, external_links = extract_links(start_url)

    node = {
        "url": start_url,
        "internal": [],
    }

    if include_external:
        node["external"] = external_links

    for link in internal_links:
        if link not in visited:
            child_node = crawl_website(link, max_depth=max_depth - 1, visited=visited,
                                       include_external=include_external)
            if child_node:
                node["internal"].append(child_node)

    return node
