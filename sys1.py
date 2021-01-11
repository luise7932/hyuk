import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(),end = " ") # 명령 행에 입력된 소문자를 대문자로 교체해주는 함수. end 함수는 반복문 한번 끝날때마다 줄 바꾸기