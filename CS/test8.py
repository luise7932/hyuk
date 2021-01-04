marks = [90, 25, 46, 67, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print(f"{number}번 학생 합격")
    else:
        print(f"{number}번 학생 불합격")

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print(f"{number}번 학생 합격 ")

add = 0
for i in range(0,10):
    add += i

print(add)
