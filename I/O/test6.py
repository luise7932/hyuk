
""" 함수 내부에서 외부의 변수를 변경하는 방법 """
# return 사용하기
a = 1


def vartest(a):
    a = a+1
    return a


a = vartest(a)
print(a)  # vartest에서 a를 리턴하였으니 함수 외부의 a도 변함

# global 명령어 사용하기
a = 1


def vartests():
    global a    # global은 함수 안에서 함수 밖의 변수를 직접 사용하겠다는 뜻. 하지만 함수는 독립적인게 좋기때문에 비추
    a += 1


vartests()
print(a)
""" lambda 함수는 함수 생성시 사용하는 예약어로 def와 동일한 역할을 한다. 함수를 한줄로 만들때 사용. """
def add(a, b): return a+b  # def add(a,b): return a+b와 같다.


result = add(3, 4)
print(result)
