def add(a, b):
    return a+b


result = add(3, 5)  # a,b에 3,5를 전달하여 매개변수 지정
print(result)
# -----------------------------------------------------------


def add_many(*args):    # 다수의 매개변수 지정이 필요할때
    result = 0
    for i in args:  # 다수의 매개변수들이 튜플args가 되어 for문 반복실행
        result += i
    return result


result = add_many(1, 2, 3)    # 함수에 1,2,3 세 개의 매개변수 지정
print(result)
# -----------------------------------------------------------


def add_mul(choice, *args):  # 첫번째 매개변수로 add일지 mul일지 지정
    if choice == "add":  # add일 시 for문을 통한 모두 합
        result = 0
        for i in args:
            result += i
    elif choice == "mul":   # mul일 시 for문을 통한 모두 곱
        result = 1
        for i in args:
            result *= i
    return result


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)
