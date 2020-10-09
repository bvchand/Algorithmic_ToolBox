# python3
import random


def max_pairwise_product(numbers):
    max_product = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            max_product = max(max_product, numbers[i] * numbers[j])
    print(max_product)


def random_inputs(n):
    rand_list = []
    for x in range(0, n):
        rand_list.append(random.randint(1, 100))
    print(rand_list)
    return rand_list


if __name__ == '__main__':
    # number = int(input())
    i = 1
    while i == 1:
        number = random.randint(1, 10)
        print(number)
        max_pairwise_product(random_inputs(number))