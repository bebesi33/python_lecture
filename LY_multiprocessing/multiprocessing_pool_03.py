import multiprocessing
from functools import partial


def square_example(n: int, multiplier: int) -> int:
    """A simple function to calculate squares, so
    one can test the multiprocessing in action

    Args:
        n (int): the input integer
        multiplier (int): some arbitrary multiplier

    Returns:
        int: the square of a number
    """
    return n * n * multiplier


if __name__ == "__main__":
    # Create a pool of 2 worker processes
    # Here the number of processes is set to a fix number
    # Many times however we check the number of available cores
    # and use the number of available cores - 1 processes
    # 1 cpu core is left for sytem and background proceses...
    num_cores = multiprocessing.cpu_count()
    print(f"The number of available cores is {num_cores}.")

    # some trickery is needed, as the map takes only one function and 1 list of elements
    # we wrap the original function into a new one, and we set the 2nd, 3rd ... etc. values
    # to the desired value
    func_with_multiplier = partial(square_example, multiplier=3)

    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(func_with_multiplier, range(20))

    print(results)
