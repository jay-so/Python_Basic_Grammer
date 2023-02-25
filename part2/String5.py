#문자열 인덱싱과 슬라이싱
a = "Life is too short. You need Python"
print(a[3])

#문자열 인덱싱 활용하기
print(a[0])
print(a[12])
print(a[-1])

#문자열 슬라이싱
a = "Life is too short. You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

#문자열 슬라이싱 - 간소화
print(a[0:4])
print(a[0:3])

#문자열 슬라이싱하는 방법
print(a[0:5])

print(a[0:2])
print(a[5:7])
print(a[12:17])

print(a[19:])
print(a[:17])
print(a[:])
a[19:-7]


#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)


#슬라이싱으로 문자열 나누기 - 심화
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)