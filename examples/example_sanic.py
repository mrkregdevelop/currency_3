import httpx
import requests
from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):

    async with httpx.AsyncClient() as client:
        r = await client.get('https://www.wikipedia.com.ua/')
    # r = requests.get('https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0')

    return text(str(r.status_code))
