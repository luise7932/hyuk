money = int(input("적금 액수를 설정해주세요 : "))
rate = float(input("연 이율을 설정해주세요 : "))
result = money * 2
year = 0
while money <= result:
    money += money * (rate * 0.01)
    year += 1
    
print(f"적금 만기 후 금액은 {int(money)}이며 {year}년 후 만기입니다.")
