import threading
import os

def worker():
    thread_name = threading.current_thread().name
    thread_id = threading.get_native_id()
    print(f"{thread_name} (ID: {thread_id}) started.")
    
    # Perform a CPU-intensive task
    total = 0
    for i in range(10_000_000_000):
        total += i
    
    print(f"{thread_name} (ID: {thread_id}) finished. Total: {total}")

def main():
    num_cores = os.cpu_count()
    print(f"Available Cores: {num_cores}")

    threads = []
    for i in range(num_cores):
        thread = threading.Thread(target=worker, name=f"Thread-{i}")
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
