# Python3
def max_loot(total_capacity, ratio_list):
    total_value = 0
    for val, wt in ratio_list:
        if total_capacity == 0:
            return '%.4f' % total_value
        amt = min(wt, total_capacity)
        total_value += amt*val/wt
        total_capacity -= amt
    return '%.4f' % total_value


if __name__ == "__main__":
    items, total_wt = [int(x) for x in input().split()]
    lst = []
    if total_wt == 0:
        print(0.0000)
        quit()
    for i in range(items):
        v, w = [int(x) for x in input().split()]
        if v == 0:
            continue
        lst.append((v, w))
    lst.sort(key=lambda x: x[0]/x[1], reverse=True)
    print(max_loot(total_wt, lst))








