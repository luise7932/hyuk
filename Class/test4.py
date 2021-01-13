class FourCal:
    def setdata(self, first, second):   # 클래스 안에 구현된 함수를 메소드라고 한다. 또한 self는 자기 자신을 매개변수로 전달하는 것
        self.first = first              # a.first = 4가 된다
        self.second = second

a = FourCal()
FourCal.setdata(a, 4, 2)                # 이렇게 호출할 수도 있는데 이러면 첫번째 매개변수 self에 a를 전달해줘야한다.
