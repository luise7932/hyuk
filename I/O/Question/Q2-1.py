def avg(*x):
    result = 0
    for i in x:
        result += i
    avg = result / len(x)
    return avg


print("평균 값을 구할 값들을 입력하시오.")
while True:
    if avg(input()) == '':
        break
     
     

print(result)
