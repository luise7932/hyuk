import time                             # 시간관련 모듈.+
print(time.time())                      # UTC를 사용하여 현재시간을 실수 형태로 반환한다.   
                                        # 1970년 1월 1일을 기준으로 지난시간을 초 단위로 반환
print(time.localtime(time.time()))      # time.time이 돌려준 실수값을 사용하여 월, 일, 시, 분, 초 등의 형태로 변환해준다.
print(time.asctime(time.localtime(time.time())))    # time.localtime에서 반환된 튜플 값을 인수로 받아 보기 쉽게 반환해준다.
print(time.ctime())                     # 상단 함수를 간편하게 표시 가능. 다른 점은 항상 현재 시간만을 반환 할 수 있다.
print(time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())))
                                        # 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷 코드 제공.
for i in range(10):                     # 일정한 시간 간격을 두고 루프를 실행할 수 있다.
    print(i)
    time.sleep(1)                       # 1초 간격으로 숫자 출력.

import calendar
print(calendar.calendar(2021))          # 그 해 전체 달력을 출력.
print(calendar.prmonth(2021, 2))        # 2월의 달력을 출력.
print(calendar.monthrange(2021, 2))     # 입력받은 달의 1일이 무슨 요일인지와 달이 며칠까지 있는지 튜플형태로 보여줌.