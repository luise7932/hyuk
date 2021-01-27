try:
    a = [1, 2]
    print(a[3])
    4/0
# 2개 이상의 오류를 동일하게 처리하기 위해서는 괄호를 사용하여 묶어 처리한다.
except (ZeroDivisionError, IndexError) as e:
    print(e)

try:
    f = open("존재하지않는파일", 'r')
except FileNotFoundError:
    pass                                        # pass를 사용하여 오류를 회피할 수 있음.
