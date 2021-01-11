def print_kwargs(**kwargs): # 매개변수 앞에 **을 붙이며 딕셔너리가 되어 키=밸류 형태의 결괏값이 딕셔너리에 저장됨
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo',age=3)