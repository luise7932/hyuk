f = open('foo.txt','w')
try:
    a = 0                   # 무언가를 수행
finally:
    f.close()               # 예외발생 여부와 상관없이 finally 절에서 f.close()로 열린 파일을 닫을 수 있다.