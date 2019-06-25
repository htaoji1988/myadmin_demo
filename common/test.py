from functools import wraps


def zhuangshi(f):
    @wraps(f)
    def new_add():
        return f(1,2)

    return new_add


@zhuangshi
def add(x: int, y: int):
    return x + y


print(add(3, 4))
