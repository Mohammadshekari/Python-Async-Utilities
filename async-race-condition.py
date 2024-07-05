import asyncio
import time

counter_with_sleep = 0
counter = 0


async def increase_counter_with_sleep():
    global counter_with_sleep
    for _ in range(100):
        tmp = counter_with_sleep
        await asyncio.sleep(0.000000001)  # Use async sleep, so here we have context switch
        counter_with_sleep = tmp + 1


async def increase_counter():
    global counter
    for _ in range(100):
        tmp = counter
        time.sleep(0.000000001)  # Use sync sleep, no context switch
        counter = tmp + 1


async def main():
    print("Starting to increasing comparison...")
    tasks = [increase_counter() for _ in range(10)]
    await asyncio.gather(*tasks)
    print("Increase number to 1000 with Sync  sleep: ", counter)

    print('=*=' * 20)

    tasks = [increase_counter_with_sleep() for _ in range(10)]
    await asyncio.gather(*tasks)
    print("Increase number to 1000 with Async sleep: ", counter_with_sleep)

    print('=*=' * 20)

    print("""Second value is 100!
because when we use async sleep, Context switch happened and
the value that stored in tmp wont be aware of increase of counter by other tasks!
and all of 10 tasks will copy the first value of counter, so the counter will increase only one time in the loop!
""")
    print('and This is RaceCondition in AsyncTasks...')


if __name__ == '__main__':
    asyncio.run(main())
