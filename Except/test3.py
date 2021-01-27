try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
    """ a는 두개의 요소값을 가지고 있기 때문에 IndexError를 발생시키므로 인덱싱 할 수 없습니다. 라는 문자열 출력.
        인덱싱 오류가 먼저 발생했으므로 ZeroDivisionError는 발생하지 않았다. """
