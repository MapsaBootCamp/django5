from celery import shared_task
import time
import asyncio
from asgiref.sync import async_to_sync

from course.models import Course

@shared_task
def hello_task(name):
    return f"hello celery to {name}"

async def return_hello():
    print("rahmaniiii")
    await asyncio.sleep(10)
    return 'hello'


@shared_task(name="summation")
def summation(a, b):
    # time.sleep(10)
    print(async_to_sync(return_hello)())
    return a + b