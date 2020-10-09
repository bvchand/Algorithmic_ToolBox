# python3
def fibonacci(num, mod):
    fib_series = [0, 1]
    while True:
        fib_series.append((fib_series[-1] + fib_series[-2]) % mod)
        if fib_series[-2:] == [0, 1]:
            seq_len = len(fib_series) - 2
            break
    idx = num % seq_len
    return fib_series[idx]


if __name__ == '__main__':
    n, m = [int(x) for x in input().strip().split()]
    print(fibonacci(n, m))

