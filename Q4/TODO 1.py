import time
items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]
# Method 1: Repeated +=
def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text
# Method 2: join()
def build_join(parts):
    return ";".join(parts) + ";"
# Method 3: f-string for each line, then join()
def build_fstring(parts):
    lines = [f"{p};" for p in parts]
    return "".join(lines)
# Benchmark one method for three runs
def benchmark(function, parts, runs=3):
    times = []
for _ in range(runs):
        start = time.perf_counter()
        result = function(parts)
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    average = sum(times) / runs
    return result, times, average
sizes = [1_000, 10_000, 200_000]
for size in sizes:
    data = items[:size]
    plus_result, plus_times, plus_avg = benchmark(build_plus, data)
    join_result, join_times, join_avg = benchmark(build_join, data)
    f_result, f_times, f_avg = benchmark(build_fstring, data)
    print(f"\nNumber of lines: {size}")
    print("Same text:", plus_result == join_result == f_result)
    print("+= times:", [round(t, 4) for t in plus_times])
    print("+= average:", round(plus_avg, 4), "s")
    print("join times:", [round(t, 4) for t in join_times])
    print("join average:", round(join_avg, 4), "s")
    print("f-string times:", [round(t, 4) for t in f_times])
    print("f-string average:", round(f_avg, 4), "s")
    print("Output length:", len(join_result))
