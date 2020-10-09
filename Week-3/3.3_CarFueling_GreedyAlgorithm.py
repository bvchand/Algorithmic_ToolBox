# Python3
def car_fueling(td, mileage, no_of_stops, gas_stops):
    current_stop = 0
    total_refills = 0
    if no_of_stops == 2:
        if gas_stops[1] - gas_stops[0] <= mileage:
            return 0
    if (gas_stops[no_of_stops-1] + gas_stops[0]) != td:
        return -1
    else:
        while current_stop < (no_of_stops - 1):
            last_stop = current_stop
            while (gas_stops[current_stop + 1] - gas_stops[last_stop]) <= mileage:
                current_stop = current_stop + 1
                if current_stop == (no_of_stops - 1):   # to avoid index out of range error
                    break
            # print("current_stop:", current_stop)
            if current_stop == last_stop:
                return -1
            if current_stop <= no_of_stops:
                total_refills += 1
                # print("total_refills:", total_refills)
        return total_refills


if __name__ == "__main__":
    d = int(input())
    m = int(input())
    n = int(input())
    gs = [int(x) for x in input().split()]
    print(car_fueling(d, m, n, gs))
