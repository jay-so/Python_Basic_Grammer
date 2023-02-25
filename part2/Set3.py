#집합 자료형을 활용하는 방법
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합
print(s1 & s2)

#intersection 함수 활용 - 교집합
print(s1.intersection(s2))

#합집합
print(s1 | s2)

#union 함수 활용 - 합집합
print(s1.union(s2))

#차집합
print(s1 - s2)

#difference함수 활용 - 차집합
print(s1.difference(s2))
print(s2.difference(s1))