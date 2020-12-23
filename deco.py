'''def test_decorator(func):
    def function_wrapper(x):
        print('Before Calling' + func.__name__)
        res=func(x)
        print('After calling' + func.__name__)
    return function_wrapper

@test_decorator

def sqr(n):
    return n**2

sqr(12)'''


def lowercase_decorator(function):
    def wrapper():
        func =  function()
        make_lowercase = func.lower
        return make_lowercase

    return wrapper

def split_string(function):
    def wrapper():
        func=function()
        split_string = func.split() 
        return split_string

    return wrapper
@split_string
@lowercase_decorator

def test_func():
    return 'PYTHON IS A HIGH LEVEL LANGUAGE'
test_func()









