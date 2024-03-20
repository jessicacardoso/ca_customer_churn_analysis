import functools
import pickle


def lru_cache_disk(maxsize=None, typed=False, filename="/tmp/cache.pickle"):
    def decorator(func):
        cache = {}
        try:
            with open(filename, "rb") as f:
                cache = pickle.load(f)
        except FileNotFoundError:
            pass

        @functools.lru_cache(maxsize=maxsize, typed=typed)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                return cache[key]
            else:
                result = func(*args, **kwargs)
                cache[key] = result
                with open(filename, "wb") as f:
                    pickle.dump(cache, f)
                return result

        return wrapper

    return decorator
