from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("***start execution***")
        result=func(*args,**kwargs)
        print("***end execution***")
        return result
    return wrapper


@log_execution
def test_1():
    """This is test number one"""
    print(test_1.__name__)
    print(test_1.__doc__)
    print("run logging test")


@log_execution
def test_2(name):
    """this is test number two"""
    print(test_2.__name__)
    print(test_2.__doc__)
    print(f"Testing loging for {name}")

@log_execution
def add(a,b):
    """this is test number three
       THIS IS add TEST
    """
    
    print(add.__name__)
    print(add.__doc__)
    return a+b
test_1()

test_2("Ahmed")

result= add(10,3)
print(result)