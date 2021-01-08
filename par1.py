import ray
import time

ray.init(ignore_reinit_error=True)

@ray.remote
def f(x):
    return x*x

futures = [f.remote(i) for i in range(1000)]
a = ray.get(futures)
print(a)
with open('myfile', 'w') as f:
    f.write(str(a))
