def is_greater_or_equal(digit, max_digit):
    if str(digit)+str(max_digit) >= str(max_digit)+str(digit):
        return True
    else:
        return False


def largest_number(digits):
    answer = []
    while digits:
        max_digit = 0
        for digit in digits:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        digits.remove(max_digit)

    for x in answer:
        print(x, end='')


if __name__ == '__main__':
    n = int(input())
    no = [int(x) for x in input().split()]
    largest_number(no)
