def max_ad_revenue(no_of_slots, slot_price, avg_clicks):
    revenue = 0
    last = 0
    # count = 0
    # for i in slot_price:
    #     for j in avg_clicks:
    #         count += 1
    #         if (i*j >= i*last) and (count <= 3):
    #             revenue += i*j
    #             # print(i, j, revenue)
    #             avg_clicks.remove(j)
    #             count
    #             if len(avg_clicks) < 1:
    #                 break
    #             last = avg_clicks[0]
    #
    #
    # return revenue

    for i in range(0, len(slot_price)):
        print("i", i)
        # last = 0
        for j in range(0, len(avg_clicks)-1):
            print("j", j)
            if (slot_price[i]*avg_clicks[j]) >= (slot_price[i]*avg_clicks[last]):
                revenue += slot_price[i]*avg_clicks[j]
                print("i, j, rev : ", slot_price[i], avg_clicks[j], revenue)
                avg_clicks.pop(j)
            if len(avg_clicks) == 1:
                last = avg_clicks[0]
            if len(avg_clicks) > 1:
                last = avg_clicks[j+1]
    return revenue


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort(reverse=True)
    # print("a:", a)
    b.sort(reverse=True)
    # print("b:", b)
    print(max_ad_revenue(n, a, b))
