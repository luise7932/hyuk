def avg(x):
    result = 0
    for i in x:
        result += int(i)
    avg = result / len(x)
    return avg

a = []
i = 0
print("평균 값을 구할 값들을 입력하시오.")
while True:
    a.append(input())
    if a[i] == '':
        a.pop()
        break
    i += 1
       
     
result = avg(a)
print(result)
