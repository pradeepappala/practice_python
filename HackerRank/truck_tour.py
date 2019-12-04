import os


#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    total_fuel = sum([i[0] for i in petrolpumps])
    total_distance = sum([i[1] for i in petrolpumps])

    # failure case
    if total_fuel < total_distance:
        return -1

    size = 0
    start_index = 0
    curr_index = 0
    curr_fuel = 0
    curr_distance = 0
    while size < len(petrolpumps):
        if curr_fuel < curr_distance:
            # if cummilative sum of fuel is less than distance
            # remove first element and increase index by 1
            curr_fuel -= petrolpumps[start_index][0]
            curr_distance -= petrolpumps[start_index][1]
            start_index += 1
            size -= 1
        else:
            # cummilative sum
            curr_fuel += petrolpumps[curr_index][0]
            curr_distance += petrolpumps[curr_index][1]
            curr_index += 1
            curr_index = curr_index % len(petrolpumps)
            size += 1

    return start_index


if __name__ == '__main__':

    petrolpumps = [[4,5], [8,5], [3,8], [9,6]]

    result = truckTour(petrolpumps)

    print(result)
