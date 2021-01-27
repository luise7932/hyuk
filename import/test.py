print(abs(3))                       # 어떤값을 받았을 때, 절댓값을 돌려주는 함수

print(all([1, 2, 3]))               # 반복가능한 자료형을 인수로 받으며, 요소가 모두 참이면 True 반환.

print(any([0, ""]))                  # 하나라도 참이면 True 반환.

print(chr(97))                      # 아스키 코드 값을 입력받아 코드에 해당하는 문자 출력

""" print(dir([test, test2]))            # 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌. """

print(divmod(7, 3))                  # 2개의 숫자를 받고, a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려줌.

# 순서가 있는 자료형을 입력받아 인덱스 값을 포함하는 enumerate 객체로 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)