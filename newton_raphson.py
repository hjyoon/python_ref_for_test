def sqrt2_newton(initial_guess=1.0, max_iter=10, tol=1e-12):
    """
    뉴턴 방법으로 sqrt(2)를 구하는 예시.
    :param initial_guess: 초기값
    :param max_iter: 최대 반복 횟수
    :param tol: 오차 허용 범위 (변화량이 tol 이하이면 중단)
    :return: sqrt(2)에 대한 근사값
    """
    x = initial_guess
    for _ in range(max_iter):
        new_x = (x + 2 / x) / 2
        if abs(new_x - x) < tol:  # 수렴 판단
            return new_x
        x = new_x
    return x


# 사용 예시
approx_value = sqrt2_newton(initial_guess=1.0, max_iter=10)
print("근사값:", approx_value)
print("실제 sqrt(2):", 2**0.5)
