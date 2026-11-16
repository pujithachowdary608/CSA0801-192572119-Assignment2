from functools import lru_cache
calls = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)
n = 5
ways_memo.cache_clear()
calls = 0
print("Number of ways:", ways_memo(n))
print("Function calls:", calls)
