import asyncio
import threading
from time import time

import httpx
import requests

# async def foo():
#     print('One')
#     sleep(1)
#     print('Two')
#
#
# start = time()
#
# for _ in range(3):
#     foo()
#
# print(f'Took: {time() - start}')


# async def foo_async():
#     print('One')
#     await asyncio.sleep(1)
#     print('Two')
#
#
# async def main():
#     await asyncio.gather(foo_async(), foo_async(), foo_async())
#
# start = time()
# asyncio.run(main())
# print(f'Took: {time() - start}')

# def foo_generator():
#     for i in range(3):
#         print('1')
#         yield i
#
#
# for j in foo_generator():
#     print('2')


urls = [
    'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
    'https://www.wikipedia.com.ua/',
    'https://play.google.com/store/apps/details?id=org.wikipedia&hl=uk&gl=US&pli=1',
] * 20


# start = time()
#
# for url in urls:
#     response = requests.get(url)
#     print(response.status_code)
#
# print(f'Took: {time() - start}')


# def foo(url):
#     response = requests.get(url)
#     print(response.status_code)
#
#
# threads = []
# start = time()
#
# for url in urls:
#     th1 = threading.Thread(target=foo, args=[url])  # foo(url)
#     # th1 = threading.Thread(target=foo, kwargs={'url': url})  # foo(url=url)
#     threads.append(th1)
#     th1.start()
#
#
# for th in threads:
#     th.join()
#
# print(f'Execution time {time() - start}')

# import httpx
#
#
# async def fetch_async(url):
#     async with httpx.AsyncClient() as client:
#         r = await client.get(url)
#     print(r.status_code)
#
#
# async def main():
#     tasks = []
#
#     for url in urls:
#         tasks.append(fetch_async(url))
#
#     await asyncio.gather(*tasks)
#
# start = time()
#
# asyncio.run(main())  # event loop
#
# print(f'Took: {time() - start}')


import httpx


async def fetch_async(url: str) -> None:
    async with httpx.AsyncClient() as client:
        r = await client.get(url, timeout=30.0)
    print(r.status_code)


async def main():
    tasks = []

    for _ in range(500):
        tasks.append(fetch_async('http://127.0.0.1:8000'))

    await asyncio.gather(*tasks)

start = time()

asyncio.run(main())  # event loop

print(f'Took: {time() - start}')

'''ASGI - WSGI'''

'''sync to async'''
