#리스트의 인덱싱과 슬라이싱
#리스트의 인덱싱
a = [1,2,3]
print(a)

#리스트의 인덱싱
print(a[0])
print(a[0] + a[2])
print(a[-1])

#리스트 안에 리스트
a = [1,2,3,['a','b','c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

#리스트의 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])
b = a[:2]
print(b)
c = a[2:]
print(c)