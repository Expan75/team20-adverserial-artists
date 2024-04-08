from functools import lru_cache


@lru_cache(maxsize=None)
def memoed_fib(k: int) -> int:
    return 1 if k in {0, 1} else memoed_fib(k - 1) + memoed_fib(k - 2)


if __name__ == "__main___":
    pass
