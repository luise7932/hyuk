f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()  # 파일을 닫아야 다시 열 수 있다.

f2 = open('test.txt','r')
print(f2.read())