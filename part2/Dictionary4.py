#딕셔너리 관련 함수들
#Key 리스트 만들기(keys)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())

for k in a.keys():
    print(k)

print(list(a.keys()))

#Value 리스트 만들기(values)
print(a.values())

#Key, Value 쌍 얻기(items)
print(a.items())

#Key: Value 쌍 모두 지우기(clear)
a.clear()
print(a)

#Key로 Value얻기(get)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('name'))
print(a.get('phone'))


#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print('name' in a)
print('email' in a)