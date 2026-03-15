import heapq

pq = []

heapq.heappush(pq, (4, 5))
heapq.heappush(pq, (1,  3))
for i in range(len(pq)):
    key, value = heapq.heappop(pq)
    print(value)