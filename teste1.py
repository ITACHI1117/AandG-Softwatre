# import threading
# import time
#
# def my_function():
#     for _ in range(10):
#         print("Working...")
#         time.sleep(1)
#
# # Create a thread for your function
# my_thread = threading.Thread(target=my_function)
#
# # Start the thread
# my_thread.start()
#
# # Check if the thread is still alive (running)
# while my_thread.is_alive():
#     print("Function is still running...")
#     time.sleep(2)
#
# print("Function has completed.")

def generate_numbers():
    for i in range(1, 6):
        yield i

# Create a generator object
num_generator = generate_numbers()

# Iterate through the generator and print values one by one
for num in num_generator:
    print(num)