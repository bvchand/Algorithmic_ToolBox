# python3
def fibonacci(n):
    a = []
    a.append(0)
    a.append(1)
    # a[0] = 0
    # a[1] = 1
    for i in range(2, n+1):
        a.append(int(a[i - 1]) + int(a[i - 2]))
    print(a[n])


if __name__ == '__main__':
    # print('Enter a number:')
    user_number = int(input())
    fibonacci(user_number)
