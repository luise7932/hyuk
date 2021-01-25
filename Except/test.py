try:
    4 / 0
except ZeroDivisionError as e:      # 오류 메세지를 변수 e에 저장
    print(e)                        # 오류 발생 시 변수 e 출력
    """ 4를 0으로 나누려고 하면 ZeroDivisionError가 발생하여 except 블록이 실행되고
        변수 e에 담기는 오류메세지를 다음과 같이 출력한다. """