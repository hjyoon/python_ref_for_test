def division_to_decimal_places(numerator, denominator, decimal_places):
    integer_part, remainder = divmod(numerator, denominator)
    decimal_part = []

    for _ in range(decimal_places):
        remainder *= 10
        decimal_digit, remainder = divmod(remainder, denominator)
        decimal_part.append(decimal_digit)

        if remainder == 0:
            break

    return f"{integer_part}." + "".join(map(str, decimal_part))


print(division_to_decimal_places(1, 7, 10))  # 1/7의 결과를 최대 소수점 10자리까지 계산
