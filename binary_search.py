target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 1, 53, 98, 19, 34, 32, 7]
# m_list = [1, 7, 19, 21, 25, 27, 30, 32, 34, 37, 47, 53, 92, 94, 98] # sorted
length = len(m_list)

m_list.sort()
left = 0 
right = length-1
mid = 0

while left <= right:
    mid = (left + right) // 2
    if m_list[mid] == target: # 단순 이분탐색일 경우 도중에 빠져나올 수 있음
        break
    if m_list[mid] > target:
        right = mid - 1
    else :
        left = mid + 1

print(mid)

# 재귀를 사용한 이분탐색
def binarySearch(array, target, left, right):
    middle_idx = (left + right) // 2
    #print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        pass
        #print('answer {}'.format(middle_idx))
    elif middle > target:
        binarySearch(array, target, left, middle_idx-1)
    elif middle < target:
        binarySearch(array, target, middle_idx+1, right)
    else: 
        return False

binarySearch(m_list, target, 0, right)