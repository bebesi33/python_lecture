import multiprocessing


def square_example(n: int) -> int:
    """A simple function to calculate squares, so
    one can test the multiprocessing in action

    Args:
        n (int): the input integer

    Returns:
        int: the square of a number
    """
    return n * n


if __name__ == "__main__":
    # Create a pool of 2 worker processes
    # Here the number of processes is set to a fix number
    # Many times however we check the number of available cores
    # and use the number of available cores - 1 processes
    # 1 cpu core is left for sytem and background proceses...
    num_cores = multiprocessing.cpu_count()
    print(f"The number of available cores is {num_cores}.")
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(square_example, range(20))

    print(results)
