import asyncio
from importlib import reload


async def hello():
    await asyncio.sleep(1)
    print("Hello")
async def world():
    await asyncio.sleep(2)
    print("World")
async def main():
    await asyncio.gather(hello(), world())
# if __name__ == '__main__':
#     asyncio.run(main())

from functools import wraps
reload(wraps)
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator()
def example():
    """Docstring"""
    print('Called example function')

example()
