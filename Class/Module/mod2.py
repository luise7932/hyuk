PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):
    return a+b

if __name__ == "__main__":
    a = Math()
    print(a.solv(2))

""" sys.path를 입력하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여준다. sys.path.append를 사용하면 내가 사용하려는 모듈의
    경로를 추가하여 별도로 모듈의 루트로 이동할 필요없이 바로 불러서 사용할 수 있다. 또한 PYTHONPATH 변수를 이용하여도 추가할 수 있다. """