import asyncio
import datetime
import time


def sync_wait(number):
    time.sleep(1)
    print('Done Sync  ', number)


async def async_wait(number):
    await asyncio.sleep(1)
    print('Done Async ', number)


async def main():
    print('# Running as Sync:')
    start_of_wait = datetime.datetime.now()
    for number in range(6):
        sync_wait(number)
    end_of_wait = datetime.datetime.now()
    print("@ Time of Sync wait: ", end_of_wait - start_of_wait)

    print('=*=' * 20)

    print('# Running as Async:')
    start_of_async_wait = datetime.datetime.now()
    for number in range(6):
        await async_wait(number)
    end_of_async_wait = datetime.datetime.now()

    print("@ Time of Async wait: ", end_of_async_wait - start_of_async_wait)

    print('=*=' * 20)

    print('# Running as Async Task:')
    start_of_async_task_wait = datetime.datetime.now()
    tasks = []
    for number in range(6):
        tasks.append(async_wait(number))
    await asyncio.gather(*tasks)
    end_of_async_task_wait = datetime.datetime.now()

    print("@ Time of Async Task wait: ", end_of_async_task_wait - start_of_async_task_wait)


if __name__ == '__main__':
    asyncio.run(main())
