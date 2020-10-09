# python3
def max_pairwise_product(numbers):
    # max_product = 0
    # for i in range(len(numbers)):
    #     for j in range(i+1, len(numbers)):
    #         max_product = max(max_product, numbers[i] * numbers[j])
    # print(max_product)
    numbers.sort()
    print(numbers[-1] * numbers[-2])


if __name__ == '__main__':
    number = int(input())
    items = [int(x) for x in input().split()]
    max_pairwise_product(items)