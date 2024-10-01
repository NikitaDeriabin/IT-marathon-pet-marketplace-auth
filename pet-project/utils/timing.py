import time
import logging

logger = logging.getLogger('main')


def measure_time(func):
    async def wrapper(request, *args, **kwargs):
        start_time = time.time()

        logger.info(f"Request: {request.method} {request.url}")

        response = await func(request, *args, **kwargs)
        process_time = time.time() - start_time

        logger.info(f"Completed in {process_time:.2f}s | Status: {response.status_code}")
        return response
    return wrapper
