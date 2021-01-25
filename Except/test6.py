class myerror(Exception):               # 내장 클래스 Exception을 상속하여 예외처리를 할 수 있다.
    def __str__(self):
        return "허용되지 않는 별명입니다."
    pass


def say_nick(nick):
    if nick == "바보":
        raise myerror()
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")                         # 예외처리 안할 시 myerror발생.
except myerror as e:
    print("허용되지 않는 별명입니다.")
