def maxSatisfied( customers, grumpy, minutes) -> int:
    # customers = [1,0,1,2,1,1,7,5]
    # grumpy = [0,1,0,1,0,1,0,1]

    # assume the beginning minutes are the selected 'not grumpy days'
    n, sum_window = len(customers), 0
    for i in range(n):
        if i < minutes:
            sum_window += customers[i]
        else:
            sum_window += (1 - grumpy[i]) * customers[i]
        print('i:',i, 'sum_window:', sum_window)

    # use sliding window to calculate
    res = sum_window
    left, right = 0, minutes
    while right < n:
        # when the right boundary of the sliding window is a grumpy day, make it into not grumpy day
        if grumpy[right] == 1:
            sum_window += customers[right]
        if grumpy[left] == 1:
            sum_window -= customers[left]
        # Real-time settlement of the max res at this time
        res = max(res, sum_window)
        left += 1
        right += 1
    return res


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
index = [0,1,2,3,4,5,6,7]
print('customers:\t', customers)
print('grumpy:\t\t', grumpy)
print('index:\t\t', index)
print(maxSatisfied(customers, grumpy, 3))
