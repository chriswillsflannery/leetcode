# multi threading
import logging
import threading
import time

def thread_function(name):
  logging.info("Thread %s: starting", name)
  time.sleep(2)
  logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

  threads = list()
  for index in range(3):
    logging.info("Main   : create and start thread %d.", index)
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

  for index, thread in enumerate(threads):
    logging.info("Main   : before joining thread %d.", index)
    thread.join()
    logging.info("Main   : thread %d done", index)

# order of when threads get run determined by OS and hard to predict.

# using ThreadPoolExecutor

import concurrent.futures
import logging

if __name__  == "__main__":
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(3))
  # with block automatically joins threads at end
  # even with TPE order of execution of threads is never guaranteed