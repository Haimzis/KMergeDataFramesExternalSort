import timeit
from decorator import decorator


@decorator
def timer(func, *args):
    timer_start = timeit.default_timer()
    ret = func(*args)
    timer_stop = timeit.default_timer()
    func_timer = timer_stop - timer_start
    if ret is not None:
        return ret, func_timer
    return func_timer

# def timer(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#
#         return func(a, b)
#     return inner