""" 원래 있던 값을 유지하면서 새로운 값만 추가할 때 '추가 모드'를 이용한다. """
f = open("테스트.txt",'a')
for i in range(11,20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()