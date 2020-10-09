# python3
def fibonacci(num):
    # Pisano period modulo 10 is 60
    # Sum of n Fibonacci numbers is F(n + 2) - 1
    fib_series = [0, 1]
    if num == 0:
        return 0

    if num == 1:
        return 1

    if num > 1:
        idx_1 = num % 60
        idx_2 = (num+1) % 60
        for i in range(2, idx_1+3):
            fib_series.append((fib_series[-1] + fib_series[-2]) % 10)
        return (fib_series[idx_1] * fib_series[idx_2]) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
