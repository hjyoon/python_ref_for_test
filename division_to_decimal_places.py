def division_to_decimal_places(numerator, denominator, decimal_places):
    # 결과의 부호 결정: numerator와 denominator의 곱이 음수이면 결과는 음수
    sign = "-" if numerator * denominator < 0 else ""

    # 음수를 처리하기 위해 절대값을 사용
    numerator, denominator = abs(numerator), abs(denominator)

    integer_part, remainder = divmod(numerator, denominator)
    decimal_part = []

    for _ in range(decimal_places):
        remainder *= 10
        digit, remainder = divmod(remainder, denominator)
        decimal_part.append(digit)
        if remainder == 0:
            break

    return sign + f"{integer_part}." + "".join(map(str, decimal_part))


print(division_to_decimal_places(-50, 8, 2))  # -6.25 출력
