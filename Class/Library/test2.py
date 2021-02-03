import os                               # 환경변수나 디렉터리, 파일 등의 os자원을 제어할 수 있게 해주는 모듈이다.
print(os.environ)                       # 현재 시스템의 환경변수 값을 보여준다.
print(os.system("dir"))                 # 시스템 명령어 중 dir을 실행하는 예.
f = os.popen("dir")                     # 시스템 명령어를 실행한 결과값을 읽기모드 형태의 파일객체로 반환.
print(f.read())                         # 읽어들인 파일 객체의 내용 출력.

""" os.mkdir(dir) : 디렉토리 생성
    os.rmdir(dir) : 디렉토리 삭제. 단, 디렉토리가 비어있어야 삭제 가능
    os.inlink(file) : 파일 삭제
    os.rename(src, dst) : src 라는 이름의 파일을 dst 라는 이름으로 변경"""

import shutil
shutil.copy("test.txt","test2.txt")     # src파일을 dst로 복사한다. 만약 dst가 디렉토리라면 src 파일을 해당 디렉토리에 복사함.

import glob                             # 디렉토리에 있는 파일명들을 리스트로 만들어준다.
print(glob.glob("C:/Users/jeaim/Documents/start python/Library/*"))

import tempfile                         # 파일을 임시로 사용할 때 유용한 모듈이다.
filename = tempfile.mkstemp()           # 중복되지 않는 임시 파일을 이름을 무작위로 생성하여 반환함.
print(filename)
f = tempfile.TemporaryFile()            # 임시 저장공간으로 사용할 파일 객체를 반환. 기본적으로 바이너리 쓰기 모드를 갖는다.
f.close()                               # 닫으면 자동으로 객체는 사라짐.


