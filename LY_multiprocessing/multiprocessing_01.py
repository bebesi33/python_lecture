import multiprocessing
import time


def worker_function(name: str):
    """A function that can simulate a CPU intensive task...

    Args:
        name (str): A simple name identifier
    """
    print(f"Process {name} started. We w8 a bit...")
    time.sleep(2)
    print(f"Process {name} finished.")


if __name__ == "__main__":
    # Define the processes
    process1 = multiprocessing.Process(target=worker_function, args=("A",))
    process2 = multiprocessing.Process(target=worker_function, args=("B",))

    # Start the processes one after the other
    process1.start()
    process2.start()
    # when the start commmand issued the two processes run separately...

    # Wait for processes to finish with the joing method
    process1.join()
    process2.join()
    # The join() method is used to wait for a process to complete.
    # Specifically, it ensures that the main program waits for the child processes
    # to finish executing before it proceeds.

    print("Both processes have completed.")
