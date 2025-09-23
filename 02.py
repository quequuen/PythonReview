#자료형과 기본 연산
#논리형
a = True
b = False
b = (3 <= 7)

a = bool("")
b = bool("abc")
c = bool(0)
d = bool(1)
e = bool([])
f = bool([1,2,3])
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# ppt 9페이지 암기
# 산술 연산자
a = int(3)
b = int(2)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)


#사용자 입출력
print()
print(1)
print(1.1)
print([1,2,3])
print("123")
print("1" "2" "3")
print("1", "2", "3")
print("1" + "2" + "3")
#자동 줄 바꿈이지만 아래 처럼 줄 바꿈이 아닌 다른 걸로도 지정 가능하다.
print(1, end=" ")
print(2, end=" ")
print(3, end=" ")
# print() 함수는 어떤 타입이든 출력 가능 -> 출력 타입은 '문자열'
input()
input("점수: ")
score = input("점수: ")
score = int(input("점수: " ))
score = float(input("점수: "))
print(score)

