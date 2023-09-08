import threading
import time

def my_function():
    for _ in range(10):
        print("Working...")
        time.sleep(1)

# Create a thread for your function
my_thread = threading.Thread(target=my_function)

# Start the thread
my_thread.start()

# Check if the thread is still alive (running)
while my_thread.is_alive():
    print("Function is still running...")
    time.sleep(2)

print("Function has completed.")