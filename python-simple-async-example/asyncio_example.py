import asyncio
import time


async def do_work():
    tasks = []

    for i in range(5):
        print("doing work...")
        tasks.append(asyncio.sleep(5))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()

    asyncio.run(do_work())

    end_time = time.time()

    print(f"execution time = {end_time - start_time}")


