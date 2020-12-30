coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1  # 커피의 개수 1개씩 감소
    print("남은 커피의 양은 %d개 입니다."% coffee)
    if coffee == 0:
        print("커피가 전부 소진되었습니다. 판매 를 중지합니다.")
        break   # 프린트 후 브레이크하여 while문 종료