import heapq

pq = [3, 5, 6, 2, 7, 1, 8, 4]
heapq.heapify(pq) # queue를 힙으로 변환

a = heapq.heappop(pq) # 힙에서 최소값을 리턴하고 그 값을 힙에서 삭제
print(a)

a = pq[0] # 힙에서 최소값을 확인 (삭제X)
print(a)

heapq.heappush(pq, 0) # 힙에 값을 추가
a = heapq.heappop(pq)
print(a)

# 힙에 값을 추가하는 것과 동시에 최소값을 리턴하고 삭제 ( heappop() + heappush() 보다 더 효율적으로 동작 )
# 인자로 푸시한 새로운 값이 동시에 최소값으로 리턴 될 수 있음.
a = heapq.heappushpop(pq, 10)
print(a)
print(pq)

# 최소값을 리턴하고 삭제하며, 새로운 값을 추가. 단 힙 크기는 변경되지 않음, 고정 크기 힙을 사용할때 더 적합 ( heappop() + heappush() 보다 더 효율적으로 동작 )
# 인자로 푸시한 새로운 값은 제외한 최소값을 리턴.
a = heapq.heapreplace(pq, 20)
print(a)
print(pq)

# 정렬된 iterable 들을 병합 (sorted와 다른점은 정렬된 리스트를 반환하는게 아닌 iterator를 반환)
t1 = heapq.merge([1, 3, 5, 7], [0, 2, 4, 8], [5, 10, 15, 20]) # 이미 오름차순 으로 정렬된 iterable들을 받아서 병합
t2 = heapq.merge([7, 5, 3, 1], [8, 4, 2, 0], [20, 15, 10, 5], reverse=True) # 이미 내림차순 으로 정렬된 iterable들을 받아서 병합

a = heapq.nlargest(3, pq) # iterable에서 최대값을 순서대로 n개만큼 복사하여 리스트로 반환한다. (효율적으로 동작하려면 iterable이 heap이어야 한다.)
print(a)

a = heapq.nsmallest(3, pq) # iterable에서 최소값을 순서대로 n개만큼 복사하여 리스트로 반환한다. (효율적으로 동작하려면 iterable이 heap이어야 한다.)
print(a)