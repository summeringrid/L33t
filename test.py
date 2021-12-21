import heapq

print('hello world')

li = [4,5,7,9,1,2,6]

heapq.heapify(li)

print('after heapify the list: ', list(li))

heapq.heappush(li, 3)
print('after pushing, the list', list(li))

next_one = heapq.heappop((li))
print('the pop one:', next_one)
print('after popping ,the list', list(li))