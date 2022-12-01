def register_call(func):
    def wrapper(*args, **kwargs):
        print("call {}".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@register_call
def square(x):
    return x ** 2


print(square(2))
