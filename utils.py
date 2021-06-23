import timeit
from decorator import decorator


@decorator
def timer(func, *args):
    timer_start = timeit.default_timer()
    ret = func(*args)
    func_timer = timeit.default_timer() - timer_start
    if ret is not None:
        return ret, func_timer
    return func_timer
