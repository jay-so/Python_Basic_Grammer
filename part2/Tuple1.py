#튜플의 형태
t1 = ()
print(t1)
t2 = (1,)
print(t2)
t3 = (1,2,3)
print(t3)
t4 = 1,2,3
print(t4)
t4 = ('a','b',('ab','cd'))
print(t4)

#튜플 요소 값 삭제 시 오류
t1 = (1,2,'a','b')
#del t1[0]
#튜플 요소 값 변경 시 오류
#t1[0] = 'c'