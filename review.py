# 1. 국립환경과학원에서는 아파트에서 소음이 가장 심한 층수를 구하는 계산식을 발표했습니다.
# 소음이 가장 심한 층은 0.2467 * 도로와의 거리(m) + 4.159 입니다.
# 다음 소스코드를 완성하여 소음이 가장 심한 층수가 출력되게 만드시오.
# 단, 층수를 출력할 때는 소수점 이하 자리는 버립니다. (정수 출력)

# distance = 12
# floor = int(0.2467 * distance + 4.159)

# print(f"소음이 가장 심한 층수는 {floor} 입니다.")

print("")
# 2. L이라는 게임에서 "왜곡"이라는 스킬이 AP * 0.6 + 225의 피해를 줍니다.
# 다음 소스 코드를 완성하여 스킬의 피해량이 출력되도록 하시오.

# ap = 13
# damage = ap * 0.6 +225

# print(f"왜곡 스킬의 피해량은 {damage}입니다.")

print("")
# 3. 정수 3개를 입력받아 합을 출력하시오

# a = int(input("정수를 입력하시오 :"))
# b = int(input("정수를 입력하시오 :"))
# c = int(input("정수를 입력하시오 :"))

# rs = a+b+c

# print(f"입력받은 a : {a}, b : {b}, c : {c} 의 합은 {rs} 입니다.")

print("")
# 4. 국어, 영어, 수학, 과학 점수를 입력받고 평균을 출력하시오.

# korea = int(input("국어점수 : "))
# english = int(input("영어점수 : "))
# math = int(input("수학점수 : "))
# science = int(input("과학점수 : "))

# avg = (korea+english+math+science)/4

# print(f"점수의 평균은 {avg} 입니다.")

print("")
# 5. 출력 형식을 2021. 09. 14 00:32:49 로 하여 출력하시오.
# year = '2021'
# month = '09'
# date = '14'
# hour = '00'
# minute = '32'
# second = '49'

# print(f"{year}. {month}. {date} {hour}:{minute}:{second}")

print("")
# 6. 국어, 영어, 수학, 과학 점수를 입력받고 평균을 구하고
# 평균이 60점 이상이면서 한 과목이라도 40점 이하가 아니어야 합격일 때
# 입력받은 점수가 합격인지 불합격인지 출력하시오.

# korean = int(input("국어점수 : "))
# english = int(input("영어점수 : "))
# math = int(input("수학점수 : "))
# scince = int(input("과학점수 : "))

# sum = korean + english + math + scince

# avg = sum / 4

# if avg >= 60 and korean > 40 and english > 40 and math > 40 and scince > 40:
#     print("합격")
# else:
#     print("불합격")

print("")
# 7. range 함수를 사용하여 [5, 3, 1, -1, -3, -5, -7, -9] 리스트를 만드시오.

# li = list(range(5, -10, -2))

# print(list(li))
# print(type(li))
print("")
# 8. 정수를 입력받고, range의 시작하는 숫자는 -10, 끝나는 숫자는 10이며 입력된 정수만큼 증가하는 숫자가 들어가도록 튜플을 만드시오.
# ex) 2 입력 (-10, -8, -6, -4, -2, 0, 2, 4, 6, 8)

# n = int(input("정수입력 : "))
# n2 = tuple(range(-10, 11, n))
# print(n2) 
# print(type(n2))

print("")
# 9. 다음 소스코드를 완성하여 x의 값이 10이 아닐 때 'OK'가 출력되도록 만드시오.
# x = 5
# if x != 10:
#     print('OK')

print("")
# 10. 가격과 쿠폰 이름을 각 줄에 입력받고, Cash3000 쿠폰은 3000원, Cash5000 쿠폰은 5000원을 할인합니다.
# 할인된 가격을 출력하시오. (단, 0원 이하는 0원을 출력)
charge = int(input("가격을 입력하시오 : "))
coupon = input("쿠폰 이름을 입력하시오 : ")


if coupon == 'cash3000':
    charge -= 3000
    if charge <= 0:
        charge = 0
elif coupon == 'cash5000':
    charge -= 5000
    if charge <= 0:
        charge = 0
print(f"{charge}원")