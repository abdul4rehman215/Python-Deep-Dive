# pdb_debugging.py

def divide_numbers(a, b):
    import pdb; pdb.set_trace()
    return a / b

divide_numbers(10, 0)
