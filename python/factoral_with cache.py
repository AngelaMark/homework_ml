import time
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        print("Defaults: ", method.__defaults__)
        return result

    return timed

@timeit
def factorial(n, cache={}):
    assert isinstance(n, int)
    assert n > 0
    
    fact_n = cache.get(str(n))
    if fact_n:
        return fact_n
    if n == 1:
        return 1
    
    fact_i = n * factorial(n-1)
    cache[str(n)] = fact_i
    return fact_i



print('Factorial of 5 first time')
factorial(5)
print('Factorial of 5 second time')
factorial(5)
print('Factorial of 4 first time')
factorial(4)
