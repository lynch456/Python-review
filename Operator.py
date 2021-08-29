
#######################################
#
#        Operator
#        연산자
#
#######################################

# 산술 연산자
# 일반적인 사칙연산과 관련된 숫자(정수, 실수) 연산자
#
# + : 더하기, - : 빼기, * : 곱하기, / : 나누기, % : 나머지, // : 몫, ** : 거듭제곱


print('')
# 대입 연산자
# 변수 자신과 계산한 결과를 자기 자신에게 저장하는 연산자
#
# = : 좌항에 우항을 저장,                      += : 좌항에 우항을 더한 값을 좌항에 저장
# -= : 좌항에 우항을 뺀 값을 좌항에 저장,       *= : 좌항에 우항을 곱한 값을 우항에 저장
# /= : 좌항에 우항을 나눈 값을 좌항에 저장,     //= : 좌항에 우항을 나눈 몫을 좌항에 저장
# %= : 좌항에 우항을 나눈 나머지를 좌항에 저장, **= : 좌항에 우항을 거듭제곱한 값을 좌항에 저장


print("")
# 산술 연산자 예제 1
# 삼각형의 밑변과 높이를 입력받고 삼각형의 넓이를 출력하시오.


print("")
# 산술 연산자 예제 2
# 학생의 이름과 국어, 영어, 수학 성적을 입력 받고 합계와 평균을 출력하시오.

# 일반 산술 연산자 활용


# 대입 연산자 활용


print("")
# 산술 연산자 예제 3
# 반지름을 입력 받고 원의 둘레와 넓이를 출력하시오.


print("")
# 산술 연산자 예제 4
# 상품을 구매하고자 할때, 총 금액과 할인율, 배송료를 입력받고 결제 금액을 출력하시오.


print("")
# 비교 연산자
# 좌항을 기준으로 우항과 비교하는 연산자
#
# 조건식 또는 논리 연산에 사용되는 연산자
# 결과값은 참(True), 거짓(False)을 반환
#
# a > b : a가 b보다 크면 True, 아니면 False
# a < b : a가 b보다 작으면 True, 아니면 False
# a >= b : a가 b보다 크거나 같으면 True, 아니면 False
# a <= b : a가 b보다 작거나 같으면 True, 아니면 False
# a == b : a와 b가 같으면 True, 아니면 False
# a != b : a와 b가 다르면 True, 아니면 False


print("")
# 비교 연산자 예제 1
# 정수를 입력받고 입력받은 수가 10보다 큰지 작은지 확인하는 조건식을 작성하시오.


print("")
# 비교 연산자 예제 2
# 정수를 입력받고 입력받은 수가 5의 배수인지 아닌지 확인하는 조건식을 작성하시오.


print("")
# 비교 연산자 예제 3
# 두 개의 정수를 입력받고 입력받은 두 수의 곱이 100보다 큰지 작은지 확인하는 조건식을 작성하시오.


print("")
# 논리 연산자
# 숫자 형태(정수, 실수)를 연산하는 것이 아니라 논리는 연산하는 연산자
# 논리형태로 반환 (True, False)
#
# a 와 b는 논리형 데이터 타입
# a and b : a 와 b가 모두 True일 때 True를 반환
# a or b : a 와 b 중 하나라도 True이면 True를 반환
# not a : a 가 True 면 False, False면 True를 반환
# 조건식에 사용되는 연산자


print("")
# 논리 연산자 1
# 필기 성적과 실기 성적을 입력받고 모두 60점 이상이어야 참이되는 조건식을 작성하시오.
# take_note = int(input("필기 성적 : "))
# practical = int(input("실기 성적 : "))
# print(take_note and practical > 60)

print("")
# 논리 연산자 2
# 아이디와 비밀번호를 입력받고 입력 받은 아이디가 'busan', 비밀번호가 '1234'로 모두 같아야 참이되는 조건식을 작성하시오.
# id = input("ID : ")
# password = int(input("비밀번호 : "))
# print(id == 'busan' and password == 1234)


print("")
# 논리 연산자 3
# 나이를 입력받고 입력받은 나이가 7세 이하이거나 65세 이상이면 참이되는 조건식을 작성하시오.
# age = int(input("나이를 입력하시오 : "))
# print(age <= 7 or age >= 65)

# print("")
# 논리 연산자 4
# 연도를 입력 받고 입력받은 연도가 4의 배수이면서 100의 배수가 아니고 400의 배수일 때 참이되는 조건식을 작성하시오.
year = int(input("연도를 입력하시오 : "))
# print(year % 4 == 0 and year % 400 == 0) or year % 100 == 0
# print(year % 4 == 0 or year % 100 != 0) and year % 400 == 0
# print(year % 4 == 0 and year % 100 != 0) or year % 400 == 0
# print(year % 4 == 0 and year % 100 != 0) and year % 400 == 0
# year = int(input("연도를 입력하시오 : "))
# print(year)
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(1)
# else:
#     print(0)

print("")
# 시퀀스 연산자
# 시퀀스 : 순서가 있는 데이터 구조(리스트, 튜플, range(), 문자열)
# + : 시퀀스 연결, * : 시퀀스 반복


print("")
# 시퀀스 연산자 1
# 두 문자열을 입력받고 입력받은 문자열을 ' '(공백)으로 연결하여 출력하시오.
str1 = input("첫번째 문자열: ")
str1 = input("두번째 문자열: ")
print()

print("")
# 시퀀스 연산자 2
# 문자열과 정수를 입력받고 입력받은 문자열을 정수 횟수만큼 반복연결시켜 출력하시오.


print("")
# 삼항 연산자
# 참일때 결과 if 조건식 else 거짓일때 결과


print("")
# 삼항 연산자 1
# 나이를 입력받고 입력받은 나이가 19세 이상이면 성인, 아니면 미성년자를 출력하시오.


print("")
# 삼항 연산자 2
# 0~23 까지의 수를 입력받고 12이상이면 오전, 아니면 오후를 출력하시오.


print("")
# 삼항 연산자 3
# 정수를 입력받고 입력받은 정수가 5의 배수면 '5의 배수', 아니면 '5의 배수가 아님'을 출력하시오.
