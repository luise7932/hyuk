""" 생성자란 객체가 생성될 떄 자동으로 호출되는 메소드를 의미
    객체 초기값 설정보다 생성자를 구현하는 것이 안전함. """
class test():
    def __init__(self, first, second):      # init을 사용하면 이 메소드는 생성자가 되어 객체가 생성될 때 자동 호출 된다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = test(3,4)
print(a.add())