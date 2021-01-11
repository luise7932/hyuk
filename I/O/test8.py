f = open("테스트.txt",'w')  # 테스트.txt 열기 (없다면 생성) r=읽기 w=쓰기 a=추가
for i in range(1,11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)   # 파일에 data매개변수 입력
f.close()