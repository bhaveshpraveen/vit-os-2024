import time

def do_work():
    for i in range(5):
        print("doing work...")
        time.sleep(5)


if __name__ == "__main__":
    start_time = time.time()
    do_work()
    end_time = time.time()

    print(f"execution time = {end_time - start_time}")

