# students = 'STRING'  # iterable (__iter__)
# student_iterator = students.__iter__()  # iterator (__next__)
# print(id(students))
# print(id(student_iterator))

# for student in students:
#     print(student)


# while True:
#     try:
#         print(student_iterator)
#     except StopIteration:
#         break

# gen = (i for i in 'STRING')
# gen = [i for i in 'STRING']  # list
# gen = {i for i in 'STRING'}  # set
# gen = {i: i for i in 'STRING'}  # dict


# for i in gen:
#     print(i)
#
#
# for i in gen:
#     print(i)


# def square():
#     counter = 0
#     while True:
#         print('GEN')
#         yield counter ** 2
#         counter += 1
#
#
# s = square()
#
# for i in s:
#     print(i)

# class Browser:
#     # 250Mb
#     def open(self):
#         pass
#
#
# browsers = [Browser() for i in range(10)]
#
# for br in browsers:
#     br.open()

'''
+ - __add__
== - __eq__

__enter__
__exit__
'''
# class Connection:
#     def open(self):
#         print('OPEN')
#         return 'CONNECTION'
#
#     def close(self):
#         print('CLOSE')
#
#     def __enter__(self):
#         return self.open()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()


# with Connection() as obj:
#     print(obj)
#     1 + '1'


# from contextlib import contextmanager
#
#
# class Suppress:
#     def __init__(self, exc_type):
#         self.exc_type = exc_type
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return exc_type is not None and issubclass(self.exc_type, exc_type)
#
#
# @contextmanager
# def Suppress2(exc_type):
#     try:
#         yield None
#     except exc_type:
#         pass
#
#
# with Suppress2(TypeError):
#     print('before')
#     1 + '1'
#     print('after')

# try:
#     c = Connection()
#     obj = c.open()
#     print(obj)
#     1 + '1'
#     print('after')
# finally:
#     c.close()

from time import sleep, time
from functools import wraps


def timenew(param):
    print(param)

    def timeit(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()

            result = func(*args, **kwargs)

            end = time()
            print(f'Time: {end - start}')

            return result

        return wrapper

    return timeit


class timeit2:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        start = time()

        result = self.function()

        end = time()
        print(f'Time: {end - start}')
        return result


@timenew('PARAM')
def foo(a):
    '''
    Sleeps for a second
    :param a:
    :return:
    '''
    sleep(1)
    result = a
    return result


@timeit2
def bar():
    sleep(2)
    result = 2
    return result


print(foo(1))
print(bar())
