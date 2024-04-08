from functools import lru_cache


@lru_cache(maxsize=None)
def memoed_fib(k: int) -> int:
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return memoed_fib(k - 1) + memoed_fib(k - 2)


if __name__ == "__main___":
    pass
