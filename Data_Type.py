
#######################################
#
#        Data Type
#        데이터 타입
#
#######################################

# 데이터 타입이란?
# 프로그래밍에 사용되는 데이터는 각자의 형태가 존재
# 그 형태를 데이터 타입이라고 함
#
# 데이터 타입의 종류
# 정수형 : -4, 0, 2021
# 실수형 : 3.14, 1.00, -0.4, 0.0
# 논리형 : True, False
# 문자열형 : 'a', 'apple', 'Jiraynor', "안녕하세요"
#
# 변수나 데이터의 타입을 확인할 때는 type() 함수를 사용


print('')
# 정수형 타입
# 0, 1, -1, 300 등과 같이 소숫점이 없는 숫자 데이터 타입
# int
a = 10
print(type(a))

print('')
# 실수형 타입
# 3.14, -0.1 등과 같이 소숫점을 포함하고 있는 숫자 데이터 타입
# float
a = 10.5
print(type(a))

print('')
# 논리형 타입
# 참(True)과 거짓(False)으로 표현하는 데이터 타입
# bool
a = True
print(type(a))

print('')
# 문자열형 타입
# 하나 또는 다수의 문자로 구성된 데이터 타입
# '' 나 "" 로 묶어서 표현
# str
a = '안녕하세요'
print(type(a))

print('')
# 숫자 1과 문자열 '1'은 서로 다른 것


print('')
# 문자열 인덱싱
# 인덱스 : 순서있게 나열된 데이터의 각 요소가 존재하는 위치
# 문자열변수[인덱스번호]
# 인덱스는 0번 부터 시작
a = '123456-1234567'
print(a[5])
print(a[-5])
print('')
# 문자열 슬라이싱
# 슬라이싱 : 순서있게 나열된 데이터 중 연결된 일부 몇 요소를 자르는 것
# 문자열변수[시작인덱스 : 종료인덱스 : 증가값]
a = '123456-1234567'
print(a[0:6])
print(a[0:6:2])
print(a[-3:])
print(a[-9::2])

print('')
# 데이터 타입 예문 1
# income 변수에 정수형태의 데이터 10000000을 저장
# date 변수에 문자열 형태의 데이터 2021-08-24를 저장
# income_tax 변수에 실수형 데이터 0.06을 저장
# payment 변수에 참을 저장

income = 10000000
date = '2021-08-24'
income_tax = 0.06
payment = True


print('')
# 데이터 타입 예문 2
# 예문 1에서 만든 date 변수를 슬라이싱하여
# year 변수에 년도를 저장
# month 변수에 월을 저장
# date 변수에 일을 저장

year = (date[0:4])
month = (date[5:7])
Date = (date[8:])

print(year, month, Date)

print('')
# 형 변환
# 데이터 타입을 변환 시키는 것


print('')
# 정수형태로 형 변환
# int(변수 혹은 데이터)
a = '10'
a1 = (int(a))
print(a1, type(a1))

print('')
# 실수형태로 형 변환
# float(변수 혹은 데이터)
a = '10'
a1 = (float(a))
print(a1, type(a1))

print('')
# 논리형태로 형 변환
# bool(변수 혹은 데이터)
# 0, [], '', {} 등은 False, 나머지는 True
a = 0
b = 30
a1 = (bool(a))
b1 = (bool(b))
print(a, type(a))
print(b, type(b))
print(a1, type(a1))
print(b1, type(b1))


print('')
# 문자열 형태로 형 변환
# str(변수 혹은 데이터)


print('')
# 형 변환 예문 1
# 데이터 타입 예문 2에서 작성한
# year, month, date의 데이터 타입을 확인하고
# 정수형으로 변환하여 year_i, month_i, date_i 변수에 저장하고
# 실수형으로 변환하여 year_f, month_f, date_f 변수에 저장하시오.


print('')
# 형 변환 예문 2
# 0, 1, 2, '안녕하세요'를
# 각각 논리형태로 형 변환하여
# b1, b2, b3, b4 변수에 저장하시오.

b1 = bool(0)
b2 = bool(1)
print(b1, b2, type(b1))
print('')
# 형 변환 예문 3
# 예문 2에서 만든 b1, b2 변수를
# 문자열로 형 변환하여
# b1_str, b2_str에 저장하시오.

b1_str = (str(b1))
b2_str = (str(b2))
print(b1_str, type(b1_str))
print(b2_str, type(b2_str))
