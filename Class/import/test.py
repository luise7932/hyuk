print(abs(3))                       # 어떤값을 받았을 때, 절댓값을 돌려주는 함수

print(all([1, 2, 3]))               # 반복가능한 자료형을 인수로 받으며, 요소가 모두 참이면 True 반환.

print(any([0, ""]))                  # 하나라도 참이면 True 반환.

print(chr(97))                      # 아스키 코드 값을 입력받아 코드에 해당하는 문자 출력

""" print(dir([test, test2]))            # 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌. """

print(divmod(7, 3))                  # 2개의 숫자를 받고, a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려줌.

# 순서가 있는 자료형을 입력받아 인덱스 값을 포함하는 enumerate 객체로 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print(eval('divmod(4,3)'))          # 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 돌려줌.

# 첫번째 인수로 함수 명을, 두번째 인수로 함수에 차례로 들어갈 반복 가능 자료형을 받는다.
# 그리고 반환 값은 참인 것만 묶어서 돌려준다.
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

print(hex(234))                     # 정수 값을 입력 받아 16진수로 변환하여 반환한다.

print(id(3))                        # 객체를 입력받아 객체 고유 주소 값을 반환.

a = input()
print(a)                            # 사용자 입력을 받아 저장함.

print(int('3'))                     # 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 반환한다.


class Person:
    pass


a = Person()
# 첫번째 인수로 인스턴스, 두번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 해당 클래스의 인스턴스인지 판단.
isinstance(a, Person)

print(len("python"))                # 입력값의 길이를 반환함.

print(list("python"))               # 반복 가능한 자료형을 입력받아 리스트로 만들어 반환함.


# 함수와 반복 가능한 자료형을 입력받고, 입력받은 값의 각 요소를 함수가 수행한 결과를 묶어서 반환함.
def two_times(x): return x*2


list(map(two_times, [1, 2, 3, 4]))

print(max([1, 3, 5]))                 # 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 반환함.

print(min([1, 3, 5]))                 # 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 반환함.

print(oct(34))                      # 정수 형태의 숫자를 8진수 문자열로 반환함.

# 파일 이름과 읽기 방법을 입력받아 파일 객체를 반환함. 읽기 방법 생략시 읽기 전용.
f = open("test.txt")
# w 쓰기모드 r 읽기모드 a 추가모드 b 바이너리 모드

print(ord('a'))                     # 문자의 아스키 코드 값을 돌려주는 함수이다.

print(pow(2, 4))                     # x의y 제곱한 결과값을 반환함.

print(list(range(5)))               # 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 반환한다.
print(list(range(5, 10)))
print(list(range(1, 10, 2)))          # 1부터 10까지 2의 간격으로 출력.

print(round(4.6))                   # 숫자를 입력받아 반올림해준다.
print(round(5.678, 2))              # 소수점 2자리까지만 반올림하여 표시할 수 있다.

print(sorted("zero"))               # 입력값을 정렬한 후 결과를 리스트로 반환함.

print(str(3))                       # 문자열 형태로 객체를 반환함.
print(str('hi'.upper()))

print(sum([1, 2, 3]))                 # 입력받은 리스트나 튜블의 모든 요소의 합을 반환함.

print(tuple("abc"))                 # 반복 가능한 자료형을 입력받아 튜플 형태로 반환해준다.

print(type("abc"))                  # 입력값의 자료형이 무엇인지 알려준다.
print(type(open("test.txt")))

print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))       # 동일한 개수로 이루어진 자료형을 묶어주는 역할을 한다.
