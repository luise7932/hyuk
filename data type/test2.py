dic = {'name':'pey', 'phone':'01032237932', 'birth':'0301'}
dic['home'] = 'gimpo'
dic[3] = [1,2,3]
dic[3,4,5] = [4,5,6]
dic.keys()

for i in dic.keys():
    print(i)
for i in dic.values():
    print(i)
for i in dic.items():
    print(i)
print('name' in dic)
print('name1'in dic)
print(dic.get('name1','해당 키는 존재하지 않습니다.'))