def factorize(n):
    # 헬퍼함수 정의
    def helper(m):
        if m == 2:
            return 3
        if m == 3:
            return 5
        k = 5
        while k * k <= n:
            if n % k == 0:
                return k
            if n % (k + 2) == 0:
                return k + 2
            k += 6
        return n
        
    # result는 결과를 담는 리스트, a는 나눠볼 소인수 후보, b는 소인수의 지수
    result, a, b = [], 2, 0
    while n > 1:
        # a로 나눌 수 있는 만큼 반복하면서 지수를 늘려나간다.
        while n % a == 0:
            n, b = n // a, b + 1
        # 한 번 이상 나눴다면 (a, b) 쌍을 결과에 추가한다.
        if b > 0:
            result.append((a, b))
            b = 0
        # 다음 후보 값을 찾는다.
        a = helper(a)
    return result

print(factorize(4524)) # 소인수분해