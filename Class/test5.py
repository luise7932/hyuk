""" 생성자란 객체가 생성될 떄 자동으로 호출되는 메소드를 의미
    객체 초기값 설정보다 생성자를 구현하는 것이 안전함. """
class test():
    def __init__(self, first, second):      # init을 사용하면 이 메소드는 생성자가 되어 객체가 생성될 때 자동 호출 된다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class More(test):                           # test를 상속받는 클래스이다.
    def pow(self):
        result = self.first ** self.second  # **는 제곱이다.
        return result
""" 메서드 오버라이딩 """
class SafeMore(test):
    """
    안전장치 설정
    """
    def div(self):
        if self.second == 0:                # 부모 클래스 test에 있는 메소드를 덮어쓰기함. 이것을 메소드 오버라이딩이라고 한다.
            return 0
        else:
            return self.first / self.second


a = test(3,4)
print(a.add())
b = More(5,7)                               # test의 모든 메소드를 사용 가능하다.
print(b.add())
print(b.pow())