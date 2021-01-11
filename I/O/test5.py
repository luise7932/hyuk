def say_myself(name,old,man=True):
    """
    매개변수 초기값을 미리 지정하여 값이 항상 변하는 것이 아닐 경우에 유용하게 함.
    """
    print("나의 이름은 %s 입니다."%name)
    print(f"나이는{old}살 입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("김혁",27)