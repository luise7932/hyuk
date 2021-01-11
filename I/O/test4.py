def add_and_mul(a,b):
    return a+b, a*b # 함수의 결과값은 1개이기 때문에 튜플값 (a+b, a*b)로 반환한다.
#   return a-b 로 리턴을 한 번 더 선언하면 두번째로 선언한 해당 리턴은 무시된다.
result = add_and_mul(3,4)
print(result)

result1,result2 = add_and_mul(3,4)  # 하나의 튜플값을 2개의 결과값으로 받으려면 다음과 같이 한다.
print(result1,result2)  # 각각 7과 12를 출력하게 됨

# ---------------------------------------------------------------------

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은%s입니다."%nick)

say_nick('야호')
say_nick('바보')