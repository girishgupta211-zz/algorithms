# importing the multiprocessing module
import multiprocessing
import os


def cube(x):
    print("Worker process id for {0}: {1}".format(x, os.getpid()))
    return x ** 3


pool = multiprocessing.Pool(processes=4)
# results = [pool.apply(cube, args=(x,)) for x in range(1, 7)]
nums = [x for x in range(1, 7)]
results = pool.map(cube, nums)
print(results)
print("----  pool is done ---")


def square_list(mylist, q):
    """
    function to square a given list
    """
    # append squares of mylist to queue
    for num in mylist:
        q.put(num * num)


def cube_list(mylist, q):
    """
    function to square a given list
    """
    # append squares of mylist to queue
    for num in mylist:
        q.put(num * num * num)


def print_queue(q):
    """
    function to print queue elements
    """
    print("Queue elements:")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")


if __name__ == "__main__":
    # input list
    input_list = [1, 2, 3, 4]

    # creating multiprocessing Queue
    q = multiprocessing.Queue()

    # creating new processes
    p1 = multiprocessing.Process(target=square_list, args=(input_list, q))
    p2 = multiprocessing.Process(target=cube_list, args=(input_list, q))
    p3 = multiprocessing.Process(target=print_queue, args=(q,))

    # running process p1 to square list
    p1.start()
    p1.join()

    # running process p1 to square list
    p2.start()
    p2.join()

    # running process p2 to get queue elements
    p3.start()
    p3.join()
