import threading
import time


def square_example(n: int, result_list: list, lock: threading.Lock):
    """A simple function to calculate squares and store the result

    Args:
        n (int): the input integer
        result_list (list): a shared list to store results
        lock (threading.Lock): a lock to prevent concurrent access to result_list
    """
    print(f"Thread {threading.current_thread().name} started with number: {n}")
    result_value = n * n
    time.sleep(3)  # Simulate some delay
    print(
        f"Thread {threading.current_thread().name} finished with result: {result_value}"
    )
    with lock:
        result_list.append(result_value)


def main():
    threads = []
    result_list = []
    lock = threading.Lock()
    for i in range(10):
        thread = threading.Thread(target=square_example, args=(i, result_list, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All threads have finished.")
    print(f"Results: {str(result_list)}")


if __name__ == "__main__":
    main()
