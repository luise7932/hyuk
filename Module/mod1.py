def add(a, b):
    return a+b


def sub(a, b):
    return a-b


if __name__ == "__main__":          # 직접 이 파일을 실행할땐 참이되어 if문을 수행하지만 다른파일에서 이 모듈을 사용할땐 if문이 수행되지 않음
    print(add(1, 4))
    print(sub(4, 2))
