import multiprocessing
import os
import time

def worker():
    process_name = multiprocessing.current_process().name
    process_id = os.getpid()
    print(f"{process_name} (ID: {process_id}) started.")
    
    # Perform a CPU-intensive task
    total = 0
    for i in range(10_000_000_000):
        total += i
    
    print(f"{process_name} (ID: {process_id}) finished. Total: {total}")

def main():
    process_id = os.getpid()
    print(f"main process id: {process_id}")
    time.sleep(5)

    start_time = time.time()

    num_cores = os.cpu_count()
    print(f"Available Cores: {num_cores}")

    processes = []
    for i in range(num_cores):
        process = multiprocessing.Process(target=worker, name=f"Process-{i}")
        processes.append(process)
        process.start()
    
    # Wait for all processes to complete
    for process in processes:
        process.join()

    print(f"Time taken to finish to program: {time.time() - start_time}")

if __name__ == "__main__":
    main()