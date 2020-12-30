x = 2
y = 3
print(x>y)

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print('j' not in 'python') # 파이썬 안에 j가 없다면 bool출력

pocket = ['paper','cellphone']
if 'money' in pocket:
    print("택시를 타고 가라")

elif card: # elif를 사용함으로써 if-else 사용을 줄임
    print("택시를 타고 가라")
else:
    print("걸어가라")

score = 50
#if score >= 60:
#   message = "success"
#else:
#    message = "failure"
message = "success" if score >= 60 else "failure" # 조건부 표현식은 가독성에 유리하고 한 줄로 간단하게 작성 가능