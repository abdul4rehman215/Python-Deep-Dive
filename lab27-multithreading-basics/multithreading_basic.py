import threading

def print_numbers(thread_name, start, end):
    for number in range(start, end):
        print(f"{thread_name}: {number}")

# Create threads
thread1 = threading.Thread(
    target=print_numbers,
    args=("Thread-1", 0, 5)
)

thread2 = threading.Thread(
    target=print_numbers,
    args=("Thread-2", 5, 10)
)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads have completed execution.")
