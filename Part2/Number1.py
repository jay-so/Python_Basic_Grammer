# 파이썬 숫자형

# 정수형
a = 123
a = -178
a = 0

#실수형
a = 1.2
a = -3.45

#실수형- 소수점 표현
a = 4.24E10
a = 4.24e-10

# 8진수와 16진수
# 8진수
a = 0o177

#16진수
a = 0x8ff
a = 0xABC

#복소수
a = 1 + 2j
b = 3-4j


#복소수 - 알아두어야 할 함수
# 복소수 - real 함수 = 실수 부분을 리턴함
print(a.real)

#복소수 - imag 함수 - 복소수의 허수 부분을 리턴함
print(a.imag)


#복소수 - conjugate 함수 - 복소수의 켤레 복소수를 리턴함
print(a.conjugate())

#복소수 - abs함수 복소수의 절대값을 리턴함
print(abs(a))
