prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())   # input함수는 값을 입력받기 위한 것