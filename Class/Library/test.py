""" pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게하는 모듈이다.
    다음은 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법이다. """
import pickle
f = open("test.txt",'wb')
data = {1: 'python',2: 'you need'}
pickle.dump(data,f)
f.close()

f = open("test.txt",'rb')
data = pickle.load(f)
print(data)
