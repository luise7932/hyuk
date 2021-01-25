class Bird:
    def fly(self):
        raise NotImplementedError               # 상속받는 자식클래스가 별도로 fly함수를 구현 안할 시 오류 발생.

class Eagle(Bird):
    def fly(self):
        print("very fast")                      # 메서드 오버라이딩하여 오류 없앰.

eagle = Eagle()
eagle.fly()