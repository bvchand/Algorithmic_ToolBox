# Python3
def compute_prize(no_of_candies):
    top_prizes = []
    total_places = 1
    top_prizes.append(1)
    count = 1
    last = 0
    while count < no_of_candies:
        if top_prizes[last]+1 <= no_of_candies-count:
            top_prizes.append(top_prizes[last]+1)
            last += 1
            total_places += 1
        else:
            count = count - top_prizes[last]
            top_prizes[last] = no_of_candies - count
        count += top_prizes[last]
        if count == no_of_candies:
            break
    print(total_places)
    for x in top_prizes:
        print(x, end=" ")


if __name__ == '__main__':
    n = int(input())
    compute_prize(n)
