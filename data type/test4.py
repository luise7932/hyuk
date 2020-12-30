a = ['mark','john','bob']
b = ['phone','name','member']
dic_result = {}
while a:
    c_dic = a.pop()
    dic_result[c_dic] = b[len(a)]
print(dic_result)

c = b[:]   #리스트 전체를 가리키는 :를 넣어 복사함으로써 별개 주소의 새 리스트를 갖는다.
from copy import copy   #copy모듈을 사용하기 위한 선언
d = copy(b)
print(c)
print(b is c)
print(d is b)