# threading
import logging
import threading
import time

# def thread_function(name):
#   logging.info('thread %s: starting', name)
#   time.sleep(2)
#   logging.info('thread %s: finishing', name)

# if __name__ == '__main__':
#   format = "%(asctime)s: %(message)s"
#   logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
#   logging.info("Main   : before creating thread")
#   x = threading.Thread(target=thread_function, args=(1,))
#   logging.info("Main   : before running thread")
#   x.start()
#   logging.info("Main   : wait for thread to finish")
#   # x.join()
#   logging.info("Main   : all done")

#   logs like:

# 07:27:36: Main   : before creating thread
# 07:27:36: Main   : before running thread
# 07:27:36: thread 1: starting
# 07:27:36: Main   : wait for thread to finish
# 07:27:36: Main   : all done
# 07:27:38: thread 1: finishing

#compare against daemon thread:
def thread_function(name):
  logging.info('thread %s: starting', name)
  time.sleep(2)
  logging.info('thread %s: finishing', name)

if __name__ == '__main__':
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
  logging.info("Main   : before creating thread")
  x = threading.Thread(target=thread_function, args=(1,), daemon=True)
  logging.info("Main   : before running thread")
  x.start()
  logging.info("Main   : wait for thread to finish")
  # x.join()
  logging.info("Main   : all done")

#   12:29:38: Main   : before creating thread
# 12:29:38: Main   : before running thread
# 12:29:38: thread 1: starting
# 12:29:38: Main   : wait for thread to finish
# 12:29:38: Main   : all done

#notice here that thread1 never logs "finishing"
# because x here is a daemon thread, when __main__ eaches the end
# of its code and the program finishes, the daemon is killed

# what if we want to wait for x to stop, before exiting the program?
# to tell one thread to wait for another to finish, we call x.join()