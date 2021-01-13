result = 0

def add(num):
    global result   # 이전에 계산한 결과값을 유지하기 위해 global 선언
    result += num
    return result

print(add(3))
print(add(4))       # 기존 add함수를 사용해 result = 3에 값이 중첩된다