marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number]<60:
        continue
    print(f"{number+1}번 학생 합격")

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')