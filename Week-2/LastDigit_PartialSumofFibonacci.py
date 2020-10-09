# python3
def fibonacci(num1, num2):
    fib_series = [0, 1]
    idx_1 = num1 % 60
    idx_2 = num2 % 60
    if idx_2 < idx_1:
        idx_2 = idx_2 + 60
    # if idx_2 - idx_1

    if (idx_1 == 0 and idx_2 == 0) or (idx_1 > 2):
        partial_sum = 0
    else:
        partial_sum = 1

    for i in range(2, idx_2+1):
        fib_series.append(((fib_series[-1] % 10) + (fib_series[-2] % 10)) % 10)
        if i >= idx_1:
            partial_sum = (partial_sum + fib_series[i]) % 10
    return partial_sum


if __name__ == '__main__':
    n1, n2 = [int(x) for x in input().strip().split()]
    print(fibonacci(n1, n2))


