import threading
import time

# Define a function that will be executed in a separate thread
def thread_function(name, delay):
    print("Thread {} started".format(name))
    counter = 0
    while counter < 5:
        time.sleep(delay)
        print("Thread {}: Counter {}".format(name, counter))
        counter += 1
    print("Thread {} finished".format(name))

# Create and start multiple threads
thread1 = threading.Thread(target=thread_function, args=(1, 1))  # Create a thread with target function and arguments
thread2 = threading.Thread(target=thread_function, args=(2, 2))
thread1.start()  # Start the thread
thread2.start()

# Wait for all threads to complete
thread1.join()  # Wait for thread1 to finish
thread2.join()  # Wait for thread2 to finish

print("All threads finished")
