#제어문

#리스트 내포(List Comprehension)
#for와 새 항목 생성을 한 행에 결합하여, 각 새 항목을 자동으로 리스트에 추가
#[표현식 for 항목 in 반복가능객체 if 조건문]

values = [1,2,3,4,5,6,7]

result1 = []
for value in values:
    result1.append(value*3)

result2 = [value *3 for value in values]
result3 = [value **2 for value in values if value % 2 == 0]

print(result1)
print(result2)
print(result3)

#숫자형 리스트 + for 루프 활용

scores = []
for idx in range(1,6):
    scores.append(int(input(f"{idx}번: ")))

for idx in range(len(scores)):
    print(f"{idx+1}번 학생 점수: ", scores[idx])

avg = sum(scores)/len(scores)
max = max(scores)
min = min(scores)
print("총 평균: ",avg)
print("최고 점수: ", max)
print("최저 점수: ", min)

#range

#range()로 리스트 만들기
a = range(1,10)
b = list(a)
print(a)
print(b)
b[0] = 11
#a[0] = 11
#range는 가상 데이터를 반환하기 때문에 재할당이나 수정이 불가능함.

#range 타입의 연속된 숫자를 생성
for value in range(10):
    print(value, end="/")
print()

for value in range(1,10):
    print(value,end="/")
print()

for value in range(1,10,2):
    print(value, end="/")
print()



#선택(조건, 분기) 구조: if
#   비교 연산자, 논리 연산자(and, or, not), 멤버십 연산자(in, not in)
#반복 구조: for/ while
#기타 제어문: continue/ break/ pass

#for 활용
# 아래 코드를 for문으로 변경
scores = [] #list()

data = input("2번:")
data = int(data)
scores.append(data)

scores.append(int(input("3번:")))
scores.append(int(input("4번:")))
scores.append(int(input("5번:")))
scores.insert(0, int(input("1번:")))

number = 0
summary = 0

for score in scores:
    number += 1
    summary += score
    print(f"{number}번 학생 점수: ", score)
avg = summary/len(scores)

#집계합수 이용
avg = sum(scores)/len(scores)

print("총 평균: ", avg)





#===================================
scores = [] #list()
data = input("2번: ")
data = int(data)
scores.append(data)

scores.append(int(input("3번: ")))
scores.append(int(input("4번: ")))
scores.append(int(input("5번: ")))
scores.insert(0, int(input("1번: ")))

print("1번 학생 점수: ", scores[0])
print("2번 학생 점수: ", scores[1])
print("3번 학생 점수: ", scores[2])
print("4번 학생 점수: ", scores[3])
print("5번 학생 점수: ", scores[4])

summary = scores[0] + scores[1] + scores[2] + scores[3] + scores[4]
avg = summary/len(scores)

print("총 평균: ", avg)


#for
numbers = ['one', 'two', 'three']
for number in numbers:
    print(number.title(), end= "")
#go랑 똑같은 title 메소드! 문자열의 첫글자를 대문자로 변경 후 문자열 반환
#파이썬의 in은 js랑 다르게 인덱스가 아닌 리스트의 요소들을 하나씩 대입

#continue
print("1~10 사이의 숫자 중 홀수의 합:", end = "")
count = 0
sum = 0
while count < 10:
    count += 1
    if count % 2 ==0:
        continue
    sum += count
print(sum)

#break
print("이름 입력하세요.(단, quit 입력시 종료)")
while True:
    name = input("이름: ").strip().lower()
    if name == 'quit':
        break
    else:
        print(name)

#while
treeHit = 0 #초기(시작)값
while treeHit<10:
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print("나무가 드디어 넘어갔습니다.")

#삼항 연산자(Conditional expression)
score = 100
if score >= 60:
    message = "succ"
else:
    message = "fail"
#위의 식을 아래처럼 표현 가능
message = "succ" if score >= 60 else "fail"
#참 if 조건 else 거짓

#pass
#빈 블록이 필요한 경우
#아무런 실행을 하지 않음.
#파이썬 if문 내에 실행문을 안 쓰면 안돼서 만들어진 거
a = 0
if a<10:
    pass
else:
    print(a)
