
#######################################
#
#        Conditional
#        조건문
#
#######################################

# 들여쓰기
#
# 파이썬은 코드 블록을 구성할 중괄호를 제공하지 않아 들여쓰기로 작성된 코드만을 실행해야 할 영역으로 판단
#
# 들여쓰기 규칙
#     1. 공백(space)이나 탭(tab)을 이용하여 들여쓰기를 수행
#     2. 공백의 개수는 상관없음. (파이썬 스타일 가이드에 따르면 공백의 개수는 4개를 사용하게 되어있음)
#     3. 탭은 1개만 사용
#     4. 동일 구역에서 들여쓰기는 통일 해야함
#     5. 주로 공백 4개, 공백2개, 탭 1개 사용. (파이썬 스타일 가이드에 따라 공백 4개를 권장)

# if 문
# 조건을 만족하는지 확인하는 문법, 만족하면 실행
#
# if 조건:
#     실행문


print("")
# if 문 예제 1
# 월을 입력 받아 해당 계절을 출력하시오.
# 3~5 : 봄, 6~8 : 여름, 9~11: 가을, 12~2: 겨울
# weather = int(input("월을 입력하시오 : "))
# if weather >= 3 and weather <= 5:
#     print("봄")
# if weather >= 6 and weather <= 8:
#     print("여름")
# if weather >= 9 and weather <= 11:
#     print("가을")
# if weather == 12 and weather == 1 and weather == 2:
#     print("겨울")

print("")
# if 문 예제 2
# 1 또는 2를 입력받아 열차의 좌석 종류를 출력하시오.
# 1 : 일반실, 2 : 특실
# train = int(input("좌석 종류 : "))
# if train == 1:
#     print("일반실")
# if train == 2:
#     print("특실")

print("")
# if 문 예제 3
# 정수를 입력받아 입력받은 수가 4의 배수이면 '4의 배수', 5의 배수이면 '5의 배수'를 출력하시오.
# n = int(input("정수입력 : "))
# if n % 4 == 0:
#     print("4의 배수")
# if n % 5 == 0:
#     print("5의 배수")
print("")
# if else 문
# 이분법적 논리가 적용되는 경우 사용
# 조건이 참일 경우 if, 거짓일 경우 else
#
# if 조건:
#     실행문
# else:
#     실행문


print("")
# if else 문 예제 1
# 체온을 입력받아 체온이 36.3도 이상 36.7도 이하이면 '정상'을, 아니면 '주의'를 출력하시오.
# tem = float(input("체온을 입력하시오 : "))
# if tem >= 36.3 and tem <= 36.7:
#     print("정상")
# else:
#     print("주의")

print("")
# if else 문 예제 2
# BMI를 이용하면 자신의 체질량 지수를 확인 할 수 있다.
# 공식은 몸무게 / (신장 ** 2) 이다. 단, 신장은 m 단위
# 몸무게와 키를 입력받고
# 18.5이상 22.9이하면 '정상', 아니면 '관리 필요'를 출력하시오.
# weight = float(input("몸무게 : "))
# height = float(input("키     : "))
# BMI = weight / (height ** 2)
# print(f"BMI 수치는? {BMI}")
# if BMI >= 18.5 and BMI <= 22.9:
#     print("정상")
# else:
#     print("관리필요")

print("")
# if elif 문
# 조건이 2가지 이상 존재할 경우 사용
#
# if 조건1:
#     실행문
# elif 조건2:
#     실행문
# ...
# else:
#     실행문


print("")
# if elif 문 예제1
# 성적을 입력받아 100~90점 이상은 A, 89~80점은 B
# 79~70점은 C, 69~60은 D, 60~0점은 F,
# 100점 초과 0점 미만은 '잘못된 입력' 을 출력하시오.
# grades = int(input("성적을 입력하시오 : "))
# if grades <= 100 and grades >= 90:
#     print("학점 : A")
# elif grades <= 89 and grades >= 80:
#     print("학점 : B")
# elif grades <= 79 and grades >= 70:
#     print("학점은 : C")
# elif grades <= 69 and grades >= 60:
#     print("학점은 : D")
# elif grades <= 60 and grades >= 0:
#     print("학점은 : F")
# else:
#     print("잘못된 입력")


print("")
# if elif 문 예제 2
# BMI를 이용하면 자신의 체질량 지수를 확인 할 수 있다.
# 공식은 몸무게 / (신장 ** 2) 이다. 단, 신장은 m 단위
# 몸무게와 키를 입력받고
# 18.5미만은 '저체중', 18.5이상 23미만이면 '정상',
# 23이상 25미만은 '과체중', 25이상 30미만은 '비만 1단계'
# 30이상 40미만은 '비만 2단계', 40이상은 '심각한 비만'을 출력하시오.

# weight = float(input("몸무게를 입력하시오 : "))
# height = float(input("키를 입력하시오 : "))
# bmi = weight / (height ** 2)
# print(f"bmi 지수 : {bmi}")
# if bmi < 18.5:
#     print("저체중")
# elif bmi >= 18.5 and bmi < 23:
#     print("정상")
# elif bmi >= 23 and bmi < 25:
#     print("과체중")
# elif bmi >= 25 and bmi < 30:
#     print("비만 1단계")
# elif bmi >= 30 and bmi < 40:
#     print("비만 2단계")
# elif bmi > 40:
#     print("심각한 비만")


print("")
# if elif 문 예제 3
# 부산교통공사의 지하철 운행 교통카드 요금은 아래와 같다.
# 어른(19세 이상 65세 미만) : 1300원
# 청소년(13세 이상 18세 이하) : 1050원
# 어린이(12세 이하) : 650원
# 경로우대자(65세 이상) : 무임
# 나이를 입력받고 해당하는 나이의 지하철 운행 교통카드 요금을 출력하시오.

# age = int(input("나이를 입력하십시오 : "))
# if age >= 19 and age < 65:
#     print(f"성인입니다. 요금은 1300원 입니다.")
# elif age >= 13 and age <= 18:
#     print("청소년 입니다. 요금은 1050원 입니다.")
# elif age <= 12:
#     print("어린이 입니다. 요금은 650원 입니다.")
# else:
#     print("경로우대자 입니다. 요금은 없습니다.")


print("")
# 중첩 사용

# if elif 문 예제 4
# 성적을 입력받아 100~90점 이상은 A, 89~80점은 B
# 79~70점은 C, 69~60은 D, 60~0점은 F,
# 100점 초과 0점 미만은 '잘못된 입력' 을 출력하시오.
# 단, F를 제외한 나머지 학점에서 5점 이상이면 +를 추가하여 출력하시오.
# grades = int(input("성적을 입력하시오 : "))
# if grades <= 100 and grades >= 90:
#     if grades >= 95:    
#     print("학점 : A")
# else:
#     print("학점 : A+")
# elif grades <= 89 and grades >= 80:
#     print("학점 : B")
#     if grades >= 85:
#         print("학점 : B+")
# elif grades <= 79 and grades >= 70:
#     print("학점 : C")
#     if grades >= 75:
#         print("학점 : C+")
# elif grades <= 69 and grades >= 60:
#     print("학점 : D")
#     if grades >= 65:
#         print("학점 : D+")
# elif grades <= 60 and grades >= 0:
#     print("학점은 : F")
# else:
#     print("잘못된 입력")

print("")
# if elif 문 예제 5
# 부산교통공사의 지하철 운행 교통카드 요금은 아래와 같다.
# - 1구간
# 어른(19세 이상 65세 미만) : 1300원
# 청소년(13세 이상 18세 이하) : 1050원
# 어린이(12세 이하) : 650원
# 경로우대자(65세 이상) : 무임
# - 2구간
# 어른 : 1구간 요금 + 200원
# 청소년 : 1구간 요금 + 150원
# 어린이 : 1구간 요금 + 100원
# 나이와 구간을 입력받고 해당하는 지하철 운행 교통카드 요금을 출력하시오.
age = int(input("나이 입력 : "))
section = input("구간 입력 : ")
fee1 = 1300
fee2 = 1050
fee3 = 650
if 65 > age >= 19:
    if section == "1구간":
        charge = (f"{section} 요금은 {fee1}원 입니다.")
    else:
        charge = (f"{section} 요금은 {fee1+200}원 입니다.")
    print(charge)
elif 18 >= age >= 13:
    if section == "1구간":
        charge = (f"{section} 요금은 {fee2}원 입니다.")
    else:
        charge = (f"{section} 요금은 {fee2+150}원 입니다.")
    print(charge)
elif 12 >= age:
    if section == "1구간":
        charge = (f"{section} 요금은 {fee3}원 입니다.")
    else:
        charge = (f"{section} 요금은 {fee3+100}원 입니다.")
    print(charge)
else:
    print(f"{section} 무임입니다.")