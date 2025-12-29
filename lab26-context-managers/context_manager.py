class MyContext:
    def __enter__(self):
        print("Entering the context and allocating resources.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context and cleaning up resources.")


# Using the custom context manager
with MyContext():
    print("Running within the context block.")


# File handling using a custom context manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with FileManager("sample.txt", "w") as f:
    f.write("Hello, World!")
