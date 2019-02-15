def outer(x,y):
    def inner1():
        return x+y

    def inner2():
        return x*y

    return (inner1, inner2)

(f1,f2)=outer(10,25)
print(f1())
print(f2())


def outer1(x,y):
    def inner3():
        return x+y
    def inner4(z):
        return inner3() + z

    return inner4

f = outer1(10,25)
print(f(15))




def decor(func):
    def header():
        print("=============================================")
        func()
        print("---------------------------------------------")

    return header

@decor
def hi():
    print("Hello")

hi()



def star(func): 
    def inner(*args, **kwargs): 
        print("#" * 3) 
        func(*args, *kwargs) 
        print("#" * 3) 
    return inner

def percent(func): 
    def inner(*args, **kwargs): 
        print("%" * 3) 
        func(*args, **kwargs) 
        print("%" * 3) 
    return inner

@star 
@percent 
def printer(msg): 
    print(msg) 
    
printer("Hello")

def decorator_func(func):
    def wrapper(*args, **kwdargs):
        return func(*args, **kwdargs)
    wrapper.__name__ = func.__name__
    return wrapper


@decorator_func
def square(x):
    return x**2

print(square.__name__)



def decorator_func(func):
    def wrapper(*args, **kwdargs):
        return func(*args, **kwdargs)
    wrapper.__name__ = func.__name__
    return wrapper


@decorator_func
def square(x):
    return x**2

print(square.__name__)