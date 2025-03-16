import multiprocessing
import time


def producer(queue: multiprocessing.Queue, num: int):
    print(f"Producer {num} started.")
    for i in range(5):
        data = f"Data {i} from Producer {num}"
        queue.put(data)  # Put data into the queue
        print(f"Producer {num} produced: {data}")
    print(f"Producer {num} finished.")


def consumer(queue: multiprocessing.Queue, num: int):
    print(f"Consumer {num} started.")
    while True:
        time.sleep(1)
        data = queue.get()
        if data == "DONE":  # the "Done" signal is processed here...
            break
        print(f"Consumer {num} consumed: {data}")
    print(f"Consumer {num} finished.")


if __name__ == "__main__":
    # Queue for communication between processes
    queue = multiprocessing.Queue()

    producer1 = multiprocessing.Process(target=producer, args=(queue, 1))
    producer2 = multiprocessing.Process(target=producer, args=(queue, 2))

    consumer1 = multiprocessing.Process(target=consumer, args=(queue, 1))
    consumer2 = multiprocessing.Process(target=consumer, args=(queue, 2))

    producer1.start()
    producer2.start()
    consumer1.start()
    consumer2.start()

    producer1.join()
    producer2.join()

    # Send "DONE" signal to consumers to indicate they can stop
    queue.put("DONE")
    queue.put("DONE")

    consumer1.join()
    consumer2.join()

    print("All processes have finished.")
