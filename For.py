
#######################################
#
#        for Loop
#        for 반복문
#
#######################################

# for (횟수 지정 반복문)
#
# 반복해야 할 횟수가 정해져 있을 때 사용
# 반복가능 객체의 요소가 남아있을 때 동안 반복
#
# for 변수 in 반복가능객체:
#     반복할 문장



print("")
# 시퀀스 자료형에서의 for
# 시퀀스 자료형 : 순서가 있는(인덱스가 존재하는) 객체 (list, tuple, string, range)
# 요소를 0번 인덱스부터 차례차례 접근
# li = [1,2,3,4,5,6,7,8,9,10]
# for i in li:
#     print(i)


# print("")
# # 비시퀀스 자료형에서의 for
# # 비시퀀스 자료형 : 순서가 없는(인덱스가 존재하지 않는) 객체 (set, dictionary)
# # set 의 경우 무작위로 접근
# # dictionary 의 경우 key에 접근
# li = {1,2,3,4,5,6,7,8,9,10}
# for i in li:
#     print(i)

print("")
# range() 함수
# 정수의 값의 범위를 생성해주는 함수
# 대부분 반복할 횟수를 지정할 때 혹은 인덱스 번호로 접근할 때 사용됨
#
# range(초깃값, 종료값, 증감값)
#
# 옵션
# 초깃값 생략가능 - 생략하면 0부터 시작
# 종료값 생략 불가능
# 증감값 생략가능 - 생략하면 +1
# for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
#     for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
#         if j <= i:                # 세로 방향 변수 i만큼
#             print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print()

# x = int(input("줄 수를 입력하시오 : "))
# for i in range(5):
#     for j in range(i):
#         print("*",end="")
#         print()

print("")
# 리스트 내포
# for 반복문을 이용해서 새로운 리스트를 조금더 쉽게 만들 수 있음
# 리스트명 = [참조식 for 변수명 in 반복가능 객체 (if 조건) ]
# for i in range(0,10,1):
#     print("%d. 김익수" %i)

# for i in range(10,0,-1):
#     print("%d. 김익수"%i)

# for i in range(0,10,1):
#     print(10 - i)


print("")
# for 문 예제 1
# 두 정수 n1, n2 를 입력받고 n1 <= a < n2 에 해당하는 a의 합을 출력하시오.
# n1 = int(input("첫번째 정수를 입력하시오 : "))
# n2 = int(input("두번째 정수를 입력하시오 : "))
# total = 0
# for i in range(n1, n2):
#     total += i
# print(total)



print("")
# for 문 예제 2
# 두 정수 n1, n2 를 입력 받고 n1 <= a < n2 에 해당하는 a의 값 중 6의 배수의 합을 출력하시오.
# n1 = int(input("첫번째 정수를 입력하시오 : "))
# n2 = int(input("두번째 정수를 입력하시오 : "))
# total = 0
# for i in range(n1, n2):
#     if i % 6 == 0:
#         total += i
# print(total)

print("")
# for 문 예제 3
# 하이푼(-)을 포함한 전화번호를 입력받고 하이푼을 제외한 숫자들만 출력하시오.



print("")
# for 문 예제 4
# 연/월/일(ex : 2021/09/01)을 입력받고 /를 제외한 숫자들만 출력하시오.



print("")
# for 문 예제 5
# 구구단 2단을 출력하시오.
# 출력형태
# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 2 * 9 = 18
# for i in range(1,10):
#     print(f"2 * {i} = {2*i}")


# print("")
# # for 문 예제 6
# # 구구단 3단을 출력하시오.
# # 출력형태
# # 3 * 1 = 3
# # 3 * 2 = 6
# # ...
# # 3 * 9 = 27
# for i in range(1,10):
#     print(f"3 * {i} = {3*i}")


print("")
# for 문 예제 7
# 구구단을 2단부터 9단까지 출력하시오.
# 출력형태는 위와 동일
# for i in range(2,10):
#     print(f"{i}단")
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")


print("")
# for 문 예제 8
# * 출력으로 삼각형을 만드시오.
# 출력형태
# *
# **
# ***
# ...
# **********
for i in range(11):
    for j in range(i):
        print("*", end="")
    print()