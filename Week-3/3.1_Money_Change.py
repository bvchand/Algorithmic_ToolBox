# python3
def money_change(m):
    coin_count = 0
    while True:
        if m >= 10:
            coin_count = coin_count + int(m / 10)
            m = m % 10
        if (m >= 5) and (m < 10):
            coin_count = coin_count + int(m / 5)
            m = m % 5
        if m < 5:
            coin_count = coin_count + m
            break
    return coin_count


if __name__ == '__main__':
    money = int(input())
    print(money_change(money))
