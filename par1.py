import ray
ray.init(ignore_reinit_error=True)
print(ray.get_webui.url())
@ray.remote
def f(x):
    return x*x

# futures = [f.remote(i) for i in range(4)]
# print(ray.get(futures))