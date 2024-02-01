import multiprocessing
from time import sleep, time
import threading

import requests

#
# def slow():
#     sleep(5)
#
#
# start = time()
#
# threads = []
#
# for t in range(1, 11):
#     th1 = threading.Thread(target=slow)
#     threads.append(th1)
#     th1.start()
#
#
# for th in threads:
#     th.join()
#
# print(f'Execution time {time() - start}')

# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://www.wikipedia.com.ua/',
#     'https://play.google.com/store/apps/details?id=org.wikipedia&hl=uk&gl=US&pli=1',
# ] * 20
#
# start = time()
#
#
# def foo(url):
#     print(threading.current_thread())
#     response = requests.get(url)
#     print(response.status_code)
#
#
# threads = []
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
#
# print(threading.current_thread())
# print(f'Execution time {time() - start}')


# def countdown(n):
#     while n:
#         n -= 1
#
#
# start = time()
#
# th1 = threading.Thread(target=countdown, args=[250_000_000])
# th2 = threading.Thread(target=countdown, args=[250_000_000])
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
#
# print(f'Execution time {time() - start}')


# def countdown(n):
#     print(multiprocessing.current_process())
#
#     while n:
#         n -= 1
#
#
# if __name__ == '__main__':
#     start = time()
#
#     th1 = multiprocessing.Process(target=countdown, args=[1_000_000_000])
#     th2 = multiprocessing.Process(target=countdown, args=[1_000_000_000])
#
#     th1.start()
#     th2.start()
#
#     print(multiprocessing.current_process())
#
#     th1.join()
#     th2.join()
#
#     print(f'Execution time {time() - start}')

# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://www.wikipedia.com.ua/',
#     'https://play.google.com/store/apps/details?id=org.wikipedia&hl=uk&gl=US&pli=1',
# ] * 1000
#
#
# def foo(url):
#     response = requests.get(url)
#
#
# if __name__ == '__main__':
#
#     start = time()
#
#     with multiprocessing.Pool(10) as p:
#         print(p.map(foo, urls))
#
#     print(f'Execution time {time() - start}')


urls = [
    'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
    'https://www.wikipedia.com.ua/',
    'https://play.google.com/store/apps/details?id=org.wikipedia&hl=uk&gl=US&pli=1',
] * 30


def foo(queue):
    while True:
        url = queue.get()

        if url is None:
            break

        print(f'foo: {url}')
        response = requests.get(url)


if __name__ == '__main__':

    start = time()

    que = multiprocessing.Queue()

    pr1 = multiprocessing.Process(target=foo, args=[que])
    pr2 = multiprocessing.Process(target=foo, args=[que])
    pr1.start()
    pr2.start()

    for url in urls:
        print(f'send to foo: {url}')
        que.put(url)

    que.put(None)
    que.put(None)

    pr1.join()
    pr2.join()

    print(f'Execution time {time() - start}')
