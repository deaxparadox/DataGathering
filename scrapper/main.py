import requests 
from bs4 import BeautifulSoup
import typing
import tomllib
import queue
import asyncio

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from gather.web import html
from settings import * 

class URL:
    ...

url: URL = "https://www.digitalocean.com/community/tutorials/how-to-create-a-url-shortener-with-django-and-graphql#step-6-implementing-error-handling"


def valid_url(url: URL) -> bool:
    val = URLValidator()
    try:
        val(url)
        return True 
    except:
        return False


q: queue.Queue = queue.Queue()
q.put(url)    
async def main():
    
    if not q.empty():
        url = q.get()
        res: requests.Response = requests.get(url)
        
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            html_elements = [x for x in dir(html.elements) if x.startswith("e_")]

            for elements in html_elements:
                try:
                    founded = soup.find_all(getattr(html.elements, elements))
                    for f in founded:
                        try:
                            check = f.attrs['href']
                            # print(check)
                            if valid_url(check):
                                print(check)
                        except:
                            pass 
                except:
                    pass 


if __name__ == "__main__":
    asyncio.run(main())