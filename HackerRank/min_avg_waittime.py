#!/bin/python3

import heapq


#
# Complete the min_avg function below.
#
def min_avg(arr):
    # sort with arrival time, get first element, delete from list
    arr = sorted(arr)
    n = len(arr)
    item = arr[0]
    arr.remove(item)
    next_pizza_time = item[0] + item[1]
    wait_time = next_pizza_time - item[0]

    for i in range(1, n):
        get_sub_arr = list(filter(lambda x: x[0] <= next_pizza_time, arr))
        if not get_sub_arr:
            item = arr[0]
            next_pizza_time = item[0] + item[1]
        else:
            sort_get_sub_arr = sorted(get_sub_arr, key=lambda x: x[1])
            item = sort_get_sub_arr[0]
            next_pizza_time += item[1]

        arr.remove(item)
        wait_time += next_pizza_time - item[0]

    return wait_time // n


class MyItem:
    def __init__(self, arrival_time, cook_time):
        self.arrivalTime = arrival_time
        self.cookTime = cook_time

    def __lt__(self, other):
        return self.cookTime < other.cookTime

    def __str__(self):
        return '{} : {}'.format(self.arrivalTime, self.cookTime)


def min_avg_time(arr):
    # sort with arrival time, get first element, delete from list
    arr = sorted(arr)
    n = len(arr)
    item = arr[0]
    next_pizza_time = item[0] + item[1]
    wait_time = next_pizza_time - item[0]

    # Insert each element into heap with cook_time
    min_heap = []
    i = 1
    while i < n:
        # while current element order time is less than current pizza time
        # insert to heap
        if arr[i][0] < next_pizza_time:
            heapq.heappush(min_heap, MyItem(arr[i][0], arr[i][1]))
            i += 1
        else:
            # Process the next pizza with min time
            try:
                item = heapq.heappop(min_heap)
                next_pizza_time += item.cookTime
                wait_time += next_pizza_time - item.arrivalTime
            except IndexError:
                # heap is empty
                item = arr[i]
                next_pizza_time = item[0] + item[1]
                wait_time += next_pizza_time - item[0]
                i += 1

    while min_heap:
        # Process the next pizza with min time
        item = heapq.heappop(min_heap)
        next_pizza_time += item.cookTime
        wait_time += next_pizza_time - item.arrivalTime

    return wait_time // n


if __name__ == '__main__':

    customers = [[0, 3], [1, 9], [2, 5], [18, 3]]

    # result = min_avg(customers)
    result = min_avg_time(customers)

    print(str(result) + '\n')
