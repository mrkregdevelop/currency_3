from time import time


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print('BEFORE IN MIDDLEWARE')
        start = time()

        response = self.get_response(request)

        end = time()
        print(f'AFTER IN MIDDLEWARE {end - start}')

        # RequestResponseLog.objects.create(....)

        return response
