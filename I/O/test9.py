f = open("테스트.txt",'r')
while True:
    line = f.readline() # readline함수를 사용하여 한 줄씩 읽어들인다.
    if not line: break  # 더 이상 읽을 줄이 없으면 break
    print(line)
f.close()
# --------------------------------------------------------------------
while 1:                # True와 마찬가지로 무한반복 
    data = input()      
    if not data: break  # 입력이 없으면 반복문 종료.
    print(data)
#---------------------------------------------------------------------
f = open ("테스트.txt",'r')
lines = f.readlines()   # readlines 함수는 파일의 모든 줄을 읽어 각각의 줄을 요소로 갖는 리스트로 돌려줌.
for line in lines:
    print(line)
f.close()
#---------------------------------------------------------------------
f = open("테스트.txt",'r')
data = f.read()         # read 함수는 파일 내용 전체를 문자열로 반환한다.
print(data)
f.close()