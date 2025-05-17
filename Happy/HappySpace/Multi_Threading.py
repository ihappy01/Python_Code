import threading
import time

def letter_printing():
    for char in "ABCDE":
        print(char,flush=True)
        time.sleep(1)

def interger_printing():
    for i in range(1,6):
        print(i,flush=True)
        time.sleep(1)


# Creating 2 threads:
thread1= threading.Thread(target=letter_printing)
# thread1.start()
thread2= threading.Thread(target=interger_printing)
# thread2.start()

# Starting both thread
thread1.start()
thread2.start()

# Waiting for both thread to complete

thread1.join()
thread2.join()

print("Both thread is finished")
#
#
#
# import threading
# import time
#
# # A function to be run by each thread
# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(1)  # Simulate a delay
#
# # Create two threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_numbers)
#
# # Start the threads
# thread1.start()
# thread2.start()
#
# # Wait for the threads to complete
# thread1.join()
# thread2.join()
#
# print("Both threads have finished!")


