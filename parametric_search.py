target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 1, 53, 98, 19, 34, 32, 7]
# m_list = [1, 7, 19, 21, 25, 27, 30, 32, 34, 37, 47, 53, 92, 94, 98] # sorted
length = len(m_list)

m_list.sort()
left = 0 
right = length-1
mid = 0

def chk():
    if m_list[mid] > target:
        return True
    else:
        return False

while left <= right:
    mid = (left + right) // 2
    # if m_list[mid] == target: # 파라메트릭 서치인 경우, 이분탐색을 모두 시도해본 결과가 정답이다.(물론 예외는 있음) (단순 해당 인덱스의 정답이 아닌, 가능한 경우의 최대 또는 최소를 찾는 것이기 때문에.)
    #     break
    if chk():   # 파라메트릭 서치인 경우, 조건의 참 거짓 유무를 밝히는 것이 복잡할 수 있으므로, 함수로 빼는것이 좋다.
        right = mid - 1
    else :
        left = mid + 1

print(mid)