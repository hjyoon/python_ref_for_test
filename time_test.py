import time
import datetime
import calendar

# 1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초단위로 반환
# 시간대는 UTC(Universal Time Coordinated, 협정 세계시)를 사용
print(time.time())

# time 모듈의 localtime 함수를 사용하면 time에서 반환한 값을 날짜와 시간 형태로 변환
# 특히 localtime이라는 이름 그대로 현재 지역의 시간대를 사용
# 대한민국에서 실행했다면 UTC에 9시간을 더한 KST(Korea Standard Time, 한국 표준시)를 사용(UTC+09:00)
# 여기서 tm_wday는 요일(월요일~일요일, 0~6), tm_yday는 1월 1일부터 경과한 일수, tm_isdst는 서머타임 여부
print(time.localtime(time.time()))

# time.localtime으로 만든 객체는 time.strftime 함수를 사용하여 원하는 날짜/시간 포맷으로 출력
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))