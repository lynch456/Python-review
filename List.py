
#######################################
#
#        List
#        리스트
#
#######################################

# List (리스트)
# 여러 값을 저장할 때 사용하는 자료형
# 저장하고자 하는 데이터 형태가 다르더라도 하나의 리스트에 저장 가능
# 추가, 삭제, 수정이 자유로움
#
# 리스트명 = [v1, v2, ...]
# 리스트명 = list(반복가능한 객체)
#
# 순서가 있어서 인덱싱과 슬라이싱이 가능


print("")
# 리스트 예제 1
# 과일이라는 리스트 변수에 apple, orange, melon, banana, blueberry를 저장하고 출력하시오.
fruits = ['apple', 'orange', 'melon', 'banana', 'blueberry']
print(fruits)


print("")
# 리스트 예제 2
# 리스트 예제 1에서 생성한 과일 변수에서 3번째 위치에 있는 과일을 출력하시오.
print(fruits[2])

print("")
# 리스트 예제 3
# 리스트 예제 1에서 생성한 과일 변수에서 마지막에서 두개의 과일을 출력하시오.
print(fruits[-2:])


print("")
# list 기능(함수)
#
# 리스트는 추가, 삭제, 수정 기능을 제공해주는 함수가 존재
# 추가 함수 : 리스트명.append(value), 리스트명.insert(idx, value)
# 확장 함수 : 리스트명.expend(list)
# 삭제 : del 리스트명[idx], 리스트명.pop(idx), 리스트명.remove(value)
# 수정 : 리스트명[idx] = value


print("")
# 리스트 기능 예제 1
# 점수를 저장할 빈 리스트를 만들고 국어 점수, 영어 점수, 수학 점수를 각각 입력받고 점수 리스트에 저장한 후 출력하시오.
# score = []
# korea = int(input("국어 점수 : "))
# english = int(input("영어 점수 : "))
# math = int(input("수학 점수 : "))
# score.append(f"국어 점수 : {korea}")
# score.append(f"국어 점수 : {english}")
# score.append(f"국어 점수 : {math}")
# print(score)

print("")
# 리스트 기능 예제 2
# 리스트 기능 예제 1에서 작성한 점수 리스트에서 수학 점수를 5점 증가시킨 값으로 수정하고 리스트를 출력하시오.
# score = []
# korea = int(input("국어 점수 : "))
# english = int(input("영어 점수 : "))
# math = int(input("수학 점수 : "))
# score.append(f"국어 점수 : {korea}")
# score.append(f"국어 점수 : {english}")
# score.append(f"국어 점수 : {math+5}")
# print(score)

print("")
# 리스트 기능 예제 3
# 상품 구매 목록 리스트를 빈 리스트로 생성하고 ['비타민C', '오메가3', '홍삼', '종합 비타민']을 확장으로 추가하고 출력하시오.
# buy_goods = []
# buy_goods.extend(['비타민C', '오메가3', '홍삼', '종합 비타민'])
# print(buy_goods)

print("")
# 리스트 기능 예제 4
# 리스트 기능 예제 3에서 생성한 상품 구매 목록 리스트에서 비타민C를 제거한 리스트를 출력하시오.

# del 키워드 사용
# buy_goods = []
# buy_goods.extend(['비타민C', '오메가3', '홍삼', '종합 비타민'])
# del buy_goods[0]
# print(buy_goods)

# # .pop(idx) 사용
# goods = []
# goods.extend(['비타민C', '오메가3', '홍삼', '종합 비타민'])
# goods.pop(0)
# print(goods)


# .remove(value) 사용
# buy_goods = []
# buy_goods.extend(['비타민C', '오메가3', '홍삼', '종합 비타민'])
# buy_goods.remove('비타민C')
# print(buy_goods)

print("")
# 오름차순 정렬 : 리스트명.sort()
# 뒤집기 : 리스트명.reverse()
# 요소의 위치 반환 : 리스트명.index(value)
# 요소 개수 카운트 : 리스트명.count(value)
# 리스트 전체 길이 : len(리스트명)


print("")
# 리스트 기능 예제 5
# 978회 로또 번호는 [7, 15, 34, 1, 32, 42]이다. 로또 번호 리스트를 오름차순으로 정렬하고 출력하시오.
# lotto = [7, 15, 34, 1, 32, 42]
# lotto.sort()
# print(lotto)

print("")
# 리스트 기능 예제 6
# 출장지 순서 리스트 ['대구', '진주', '경주', '대구', '서울', '용인', '서울', '대구', '부산']에서
# 대구에 몇번 방문했는지 구하고 출력하시오.
place = ['대구', '진주', '경주', '대구', '서울', '용인', '서울', '대구', '부산']
place.count('대구')
place.count('진주')
place.count('경주')
place.count('서울')
place.count('용인')
place.count('부산')
print(f"대구에는 몇 번 갔습니까 : {place.count('대구')}번")

print("")
# 리스트 기능 예제 7
# 리스트 기능 예제 6에서 방문한 출장지를 몇곳을 방문했는지 중복을 허용해서 구하고 출력하시오.
# print(f"대구에는 몇 번 갔습니까 : {place.count('대구')}번")
# print(f"진주에는 몇 번 갔습니까 : {place.count('진주')}번")
# print(f"경주에는 몇 번 갔습니까 : {place.count('경주')}번")
# print(f"서울에는 몇 번 갔습니까 : {place.count('서울')}번")
# print(f"용인에는 몇 번 갔습니까 : {place.count('용인')}번")
# print(f"부산에는 몇 번 갔습니까 : {place.count('부산')}번")
# place2 = place.count('대구')
# print(f"대구에는 {place2}번 갔음")
length = len(place)
print(length)

print("")
# 다차원 리스트
# 리스트의 요소로 리스트를 추가하여 2차원, 3차원 형태의 다차원 리스트를 생성할 수 있음
# 리스트명 = [[v1, v2, ...], [v4, v5, ...], ...]
# 접근 방법 : 리스트명[1차원 리스트의 idx][2차원 리스트의 idx]...


print("")
# 다차원 리스트 예제 1
# 3개의 프로그래밍언어
# ['파이썬', 'Python', '보통'], ['자바', 'Java', '조금 어려움'], ['씨 언어', 'C Language', '매우 어려움']를 저장하는
# 리스트를 작성하고 출력하시오.
li = [['파이썬', 'Python', '보통'], ['자바', 'Java', '조금 어려움'],
      ['씨 언어', 'C Language', '매우 어려움']]
print(li)
print("")
# 다차원 리스트 예제 2
# 다차원 리스트 예제 1에서 작성한 리스트에서 2번째 리스트의 3번째 값을 구하고 출력하시오.

print(li[1][2])
