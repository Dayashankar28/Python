import time

def cal_time(func):
    def wrapper(*args, **kaargs):
        start_time = time.time()
        print("########################")
        print("####### Started ########")
        print("########################")
        out = func(*args, **kaargs)
        time_of_execution = time.time() - start_time
        print(f'Total time to execute is : {time_of_execution}')
        return out
    return wrapper

@cal_time
def sqr(n):
    return n * n

sqr(10)

@cal_time
def loop1(m, n):
    for i in range(500000000):
        pass
loop1("2","22")