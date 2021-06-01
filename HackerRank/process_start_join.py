import multiprocessing
import time


def my_thread(id):
    # time.sleep(5-id)
    print('In %s' % id)
    return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=my_thread, args=(i,))
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()