import time
import threading


def do_work():
    threads = []
    for i in range(5):
        print("doing work...")
        
        t = threading.Thread(target=lambda: time.sleep(5))
        threads.append(t)
        t.start()



    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    

    
if __name__ == "__main__":
    start_time = time.time()
    do_work()
    end_time = time.time()

    print(f"execution time = {end_time - start_time}")
        




