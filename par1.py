import ray
import time

ray.init(ignore_reinit_error=True, address="auto")

@ray.remote
def f(x):
    time.sleep(1)
    return x*x

futures = [f.remote(i) for i in range(1000)]
a = ray.get(futures)
print(a)
with f as open('myfile', 'w'):
    f.write(str(a))