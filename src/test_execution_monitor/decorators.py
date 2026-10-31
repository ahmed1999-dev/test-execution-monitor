from functools import wraps

test_results = []


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("***start execution***")
        result = func(*args, **kwargs)
        print("***end execution***")
        return result

    return wrapper
