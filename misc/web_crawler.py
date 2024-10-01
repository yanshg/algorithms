'''
Given a URL startUrl and an interface HtmlParser, implement a multi-threaded web crawler to crawl all links that are under the same hostname as startUrl. Return all URLs obtained by your web crawler in any order.
'''


import concurrent.futures
from typing import List

class HtmlParser:
    def getUrls(self, url: str) -> List[str]:
        # This method is provided by the problem and simulates fetching URLs from a webpage.
        pass

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url):
            return url.split('/')[2]
        
        start_hostname = get_hostname(startUrl)
        visited = set()
        visited.add(startUrl)
        queue = [startUrl]
        
        def worker(url):
            urls = htmlParser.getUrls(url)
            for next_url in urls:
                if next_url not in visited and get_hostname(next_url) == start_hostname:
                    visited.add(next_url)
                    queue.append(next_url)
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            while queue:
                futures = [executor.submit(worker, url) for url in queue]
                queue = []
                concurrent.futures.wait(futures)
        
        return list(visited)
