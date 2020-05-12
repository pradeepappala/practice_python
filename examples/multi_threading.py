import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))        # "Thread-x started!"
        time.sleep(10)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))       # "Thread-x finished!"


def main():
    t = 10
    for x in range(t):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x))  # ...Instantiate a thread and pass a unique ID to it
        mythread.run()                                     # ...Start the thread, invoke the run method
        # time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another


if __name__ == '__main__':
    main()