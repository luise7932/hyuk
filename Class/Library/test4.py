import random
print(random.random())                      # 0.0에서1.0사이의 실수 중 난수 값을 반환한다.
print(random.randint(1,10))                 # 1에서 10사이의 정수 중 난수 값을 반환한다.

def random_pop(data):
    number = random.randint(0, len(data)-1) # 0에서 매개변수 data까지의 정수 중 난수 값을 반환.
    return data.pop(number)                 # number번째 숫자를 pop 해서 반환.

if __name__ == "__main__":                  # 이 모듈을 직접 실행할 때만
    data = [1,2,3,4,5]
    random.shuffle(data)                    # 리스트의 항목을 무작위로 섞는다.
    while data:
        print(random_pop(data))             # 리스트의 요소 중 무작위로 하나 꺼내서 반환. 꺼낸 요소는 pop으로 인해 사라짐.

import webbrowser                           # 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈.
webbrowser.open("http://google.com")        # 실행 후 구글 오픈. 브라우저 열려있으면 입력한 주소로만 이동.
#webbrowser.open_new("http://google.com")   # open_new는 이미 브라우저가 실행중이더라도 새로운 창으로 연다.

