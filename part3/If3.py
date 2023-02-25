#조건문 - 비교 연산자
x = 3
y = 2
print(x>y)
print(x<y)
print(x == y)
print(x != y)

money = 2000
if(money >= 3000):
    print("택시를 타고 가라")
else:
    print("걸어가라")

#비교 연산자 - and, or, not
money = 2000
card = 1
if(money >= 3000 or card):
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#x in s, x not in s
#리스트
print(1 in [1,2,3])

print(1 not in [1,2,3])

#튜플
print('a' in ('a','b','c'))

print('j' not in 'python')

pocket = ['paper','cellphone','money']
if('money' in pocket):
    print("택시를 타고 가라")
else:
    print("걸어 가라")