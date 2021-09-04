
#######################################
#
#        Tuple
#        튜플
#
#######################################

# Tuple (튜플)
# 여러 값을 저장할 때 사용하는 자료형
# 저장하고자 하는 데이터 형태가 다르더라도 하나의 리스트에 저장 가능
# 한번 생성한 후 수정 불가
#
# 튜플명 = (v1, v2, ...)
# 튜플명 = v1, v2, ...
# 튜플명 = tuple(반복가능한 객체)
#
# 순서가 있어서 인덱싱과 슬라이싱이 가능


from typing import Tuple


print("")
# 튜플 예제 1
# Fruits라는 튜플 변수에 apple, orange, melon, banana, blueberry를 저장하고 출력하시오.

# 괄호를 이용한 방법
Fruits = ('apple, orange, melon, banana, blueberry')
print(Fruits)


# 괄호를 이용하지 않는 방법
Fruits = 'apple', 'orange', 'melon', 'banana', 'blueberry'
print(Fruits)

#  반복가능 객체를 이용한 방법
Fruits = tuple('apple')
print(Fruits)

print("")
# 튜플 예제 2
# BESPOKE라는 튜플 변수에 Refrigerator, Water Purifier, Dishwasher, Induction, Air Conditioner 를 저장하고 출력하시오.

# 괄호를 이용한 방법
BESPOKE = ('Refrigerator, Water Purifier, Dishwasher, Induction, Air Conditioner')
print(BESPOKE)
# 괄호를 이용하지 않는 방법
BESPOKE = 'Refrigerator', 'Water Purifier', 'Dishwasher', 'Induction', 'Air Conditioner'
print(BESPOKE)

#  반복가능 객체를 이용한 방법
BESPOKE = tuple('Induction')
print(BESPOKE)
