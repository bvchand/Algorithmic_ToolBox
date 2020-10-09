# python3
def fibonacci(num):
    fib = 0
    a = 0
    b = 1
    for i in range(2, num+1):
        fib = (a + b) % 10
        a = b % 10
        b = fib
    return fib

    # fib_series = [0, 1]
    # while True:
    #     fib_series.append((fib_series[-1] + fib_series[-2]) % 10)
    #     if fib_series[-2:] == [0, 1]:
    #         seq_len = len(fib_series) - 2
    #         break
    # idx = num % seq_len
    # return fib_series[idx]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
