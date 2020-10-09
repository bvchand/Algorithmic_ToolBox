# python3
def fibonacci(num):
    # Pisano period modulo 10 is 60
    # Sum of n Fibonacci numbers is F(n + 2) - 1

    fib_series = [0, 1]
    idx = num % 60

    if idx == 0:
        return 0

    if idx == 1:
        return 1

    if idx > 1:
        for i in range(2, idx+3):
            fib_series.append((fib_series[-1] + fib_series[-2]) % 10)
            # print(fib_series[i])
        sum_last_digit = (fib_series[idx + 2] - 1) if ((fib_series[idx + 2]) != 0) else 9
        return sum_last_digit


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
