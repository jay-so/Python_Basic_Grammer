#딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey':10,'julliet':99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a',2:'b'}
print(a[1])
print(a[2])

#Value와 key값을 바꾼 딕셔너리에서 값 출력
a = {'a':1,'b':2}
print(a['a'])

dic = {'name':'pey','phone':'0119993323','birth':'1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

#딕셔너리를 만들 때 주의할 사항 -1
# 중복된 키 값 사용시 이전의 값은 날라감
a = {1:'a',1:'b'}
print(a)

#딕셔너리를 만뜰 때 주의할 사항 -2
#key에는 리스트를 사용할 수 없음, 튜플은 Key로 사용할 수 있음
#a = {[1,2]:'hi'} #리스트를 키로 사용