import random


def quick_select(arr, k):
    """
    주어진 리스트 arr에서 k번째 작은 요소를 찾는 Quick Select 알고리즘 함수.
    :param arr: 숫자 리스트
    :param k: 찾고자 하는 순서 (0-indexed). 예를 들어 k=0이면 가장 작은 요소.
    :return: k번째 작은 요소
    """
    # 리스트의 길이가 1이면 유일한 요소를 반환
    if len(arr) == 1:
        return arr[0]

    # 랜덤하게 pivot 선택
    pivot = random.choice(arr)

    # pivot을 기준으로 리스트를 세 부분으로 분할
    lows = [x for x in arr if x < pivot]  # pivot보다 작은 값들
    highs = [x for x in arr if x > pivot]  # pivot보다 큰 값들
    pivots = [x for x in arr if x == pivot]  # pivot과 같은 값들

    # k번째 작은 요소가 lows에 있는 경우
    if k < len(lows):
        return quick_select(lows, k)
    # k번째 작은 요소가 pivots에 있는 경우 (즉, pivot 값이 답인 경우)
    elif k < len(lows) + len(pivots):
        return pivot
    # k번째 작은 요소가 highs에 있는 경우, k 값을 조정하여 재귀 호출
    else:
        return quick_select(highs, k - len(lows) - len(pivots))


# 사용 예시
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    kth = 2  # 0-indexed 기준: 2이면 세 번째 작은 요소
    result = quick_select(arr, kth)
    print(f"{kth+1}번째 작은 요소는 {result}입니다.")
