class Family():
    """
    클래스 변수 설정
    """
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)

Family.lastname = "박"               # 클래스 변수는 변경 가능하다. 또한 클래스로 만든 모든 객체가 같은 메모리를 공유한다.
print(a.lastname)
print(b.lastname)