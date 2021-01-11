""" with문 을 사용하면 파일 열고닫기를 자동으로 할 수 있다. """
with open("테스트.txt",'w') as f:
    f.write("test WITH")            # with문을 벗어나는 순간 자동으로close된다.
