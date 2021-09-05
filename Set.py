
#######################################
#
#        Set
#        세트
#
#######################################

# Set (세트)
# 수학의 집합개념, 중복된 값을 저장할 수 없음
# 순서가 없어서 인덱싱과 슬라이싱이 불가능
#
# 세트명 = {v1, v2, ...}
# 세트명 = set(반복가능한객체)
# 빈 세트를 선언할 때는 세트명 = {} 불가능, 세트명 = set() 가능
#
# 추가 : add()
# 삭제 : remove() - 요소가 없으면 오류를 반환
#        discard() - 요소가 없어도 오류를 반환하지 않음


print("")
# 세트 예제 1
# 리스트 변수 height = [183, 173, 166, 184, 176, 173, 176]의 중복을 제거하여 height_s 에 저장하고 출력하시오.
height = [183, 173, 166, 184, 176, 173, 176]
height_s = set(height)
print(height_s)

print("")
# 세트 예제 2
# 키를 입력 받아 세트 예제 1에서 작성한 height_s에 중복을 제거하여 저장하고 출력하시오.


print("")
# 세트 예제 3
# 키를 입력 받아 세트 예제 1에서 작성한 height_s에서 만약 요소가 없더라도
# 오류가 발생하지 않도록하여 삭제하고 출력하시오.


print("")
# 세트 예제 4
# 리스트 변수 milk = ['딸기우유', '초코우유', '딸기우유', '흰우유', '초코우유', '커피우유']의 중복을 제거하여
# milk_s 에 저장하고 출력하시오.


print("")
# 세트 예제 5
# 우유 종류를 입력 받아 세트 예제 4에서 작성한 milk_s 중복을 제거하여 저장하고 출력하시오.


print("")
# 세트 예제 6
# 우유 종류를 입력 받아 세트 예제 4에서 작성한 milk_s 만약 요소가 없더라도
# 오류가 발생하지 않도록하여 삭제하고 출력하시오.


print("")
# Set 연산 (집합 연산자 및 함수)
# 교집합 : &, intersection()
# 합집합 : |, union()
# 차집합 : -, difference()


print("")
# 세트 연산자 예제 1
# height_s2 = {183, 173, 166, 184, 177, 178} 의
# 세트 예제 1에서 작성한 height_s와의 교집합, 합집합, 차집합을 출력하시오.


print("")
# 세트 연산자 예제 2
# milk_s2 = {'커피우유', '딸기우유', '바나나우유'} 의
# 세트 예제 4에서 작성한 milk_s와의 교집합, 합집합, 차집합을 출력하시오.
