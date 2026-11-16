def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)
def ways_memo(n, memo):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = ways_memo(n - 1, memo) + ways_memo(n - 2, memo)
    return memo[n]
naive_calls = 0
memo_calls = 0
n = 25
original_result = ways_naive(n)
optimized_result = ways_memo(n, {})
print("Input:", n)
print("Original result:", original_result)
print("Original calls:", naive_calls)
print("Optimized result:", optimized_result)
print("Optimized calls:", memo_calls)
