import asyncio
import time

sync_counter = 0
async_counter = 0
lock_counter = 0


async def sync_increase():
    global sync_counter
    for _ in range(100):
        tmp = sync_counter
        time.sleep(0.000000001)  # Use sync sleep, no context switch
        sync_counter = tmp + 1


async def async_increase():
    global async_counter
    for _ in range(100):
        tmp = async_counter
        await asyncio.sleep(0.000000001)  # Use async sleep, so here we have context switch
        async_counter = tmp + 1


async def lock_increase(lock: asyncio.Lock):
    global lock_counter
    for _ in range(100):
        async with lock:
            tmp = lock_counter
            await asyncio.sleep(0.000000001)  # no context switch, because we used lock
            lock_counter = tmp + 1


async def main():
    print("Starting to increasing comparison...")
    tasks = [sync_increase() for _ in range(10)]
    await asyncio.gather(*tasks)
    print("Increase number to 1000 with Sync  sleep: ", sync_counter)

    print('=*=' * 20)

    tasks = [async_increase() for _ in range(10)]
    await asyncio.gather(*tasks)
    print("Increase number to 1000 with Async sleep: ", async_counter)

    print('=*=' * 20)

    print("""Second value is 100!
because when we use async sleep, Context switch happened and
the value that stored in tmp wont be aware of increase of counter by other tasks!
and all of 10 tasks will copy the first value of counter, so the counter will increase only one time in the loop!
""")
    print('and This is RaceCondition in AsyncTasks...\n\n')
    print('This can be Fixed with asyncio.Lock:')
    print('=*=' * 20)
    lock = asyncio.Lock()
    tasks = [lock_increase(lock) for _ in range(10)]
    await asyncio.gather(*tasks)
    print("Increase number to 1000 with Lock Async: ", lock_counter)
    print('=*=' * 20)


if __name__ == '__main__':
    asyncio.run(main())
