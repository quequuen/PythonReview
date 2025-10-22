#range 응용
scores = [100, 90, 75]
for i in range(len(scores)): #range 안에는 숫자만 들어갈 수 있음.
    print(f"{i+1} : {scores[i]}")

#리스트 내포
scores = [10, 20, 15]
offset = []
for score in scores:
    if score <= 15:
        offset.append(score/2)

offset = []
#offset1 = [for score in scores]     #나오는 value 값을 정의해주지 않으면 안됨
offset2 = [score for score in scores]
offset3 = [score / 2 for score in scores]
offset4 = [score // 2 for score in scores if score <= 15]

#print(offset1)
print(offset2)
print(offset3)
print(offset4)

# ** 가변 매개변수
def test(a, b, **kwargs): #dictionary로 들어옴
    #print(type(kwargs))
    print(kwargs)
    print(a, b)
    print(kwargs.get("loc", "-"))
    print(kwargs.get("field","-"))

test("kim", "inha", loc = "incheon")
test("lee", "younghyun", loc = "seoul")
test("park", "jungsuk", hobby = "song")


# *가변매개변수
def calc(choice, *args): #tuple로 들어옴
    print(type(args))
    print(args)
    if choice.lower() == "a":
        result = 0
        for i in args: result += i
    elif choice.lower() == "m":
        result = 1
        for i in args: result *= i
    else:
        return None
    return result


a = calc("a", 1, 2)
b = calc("m", 1, 2)
c = calc("d", 1, 2)
print(a, b, c)

#tuple
a = (1,2,['3','4'])
b = a[2]

print(b)
#tuple은 요소값을 삭제류(del)하거나 재할당할 때 오류
#튜플은 요솟값을 변경할수 없기 때문에 sort, insert, remove, pop과 같은 내장 함수가 없다.


#week04_01.py
motorcycles = ["daelim", "bmw", "yamaha",
               "suzuki", "vespa"]

#a = del morotcycles[0]
#추출 불가능! del은 순수하게 요소 삭제만을 행함.

popdata = motorcycles.pop()
print(popdata)
print(motorcycles)
#맨 뒤의 요소를 뽑아냄

motorcycles.remove("yamaha")
print(motorcycles)
#요소를 비교해서 삭제

popdata = motorcycles.pop(1)
print(popdata)
print(motorcycles)

cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyndai"]
#순서를 반전함.
#값이 아님.(원본을 손상함)

cars.reverse()
print(cars)

cars_copy = cars[:]
cars_copy.reverse()
#원래는 이런 식으로 reverse함(원본 보호)

cars_copy = sorted(cars, reverse = True)    #내림차순(역방량, desc)으로 정렬
print(cars_copy)
#정렬을 했으니까 당연히 cars랑 다르게 나오지~




#week03_04.py
test = "   JMT University   "

#str.split()메소드의 반환형 : list
#split의 기준이 없음. : 공백문자를 기준으로 쪼개버림.
print(test.split())
#split의 기준 "i"
print(test.split("i"))

#str.replace() 원문자열을 손상하지 않음
#              신규 문자열을 생성한다.
#문자열은 불변자료.
print(test.replace("University", "High School"))
print(test)


print("|" + test.strip()  + "|")
print("|" + test.lstrip() + "|")
print("|" + test.rstrip() + "|")


test = "i am a BOY."

print(test.upper())
print(test.lower())
print(test.title())
print(test.capitalize())


print("/".join(test))


print(test.find("am")) #2
print(test.find("q"))  #-1
print(test.index("am")) #2
#print(test.index("q"))  #에러


print(test.count("a"))


# 형태적 분석
# len(a)     #(모두의) 함수
# a.len()    #(누군가의/누군가만 호출) 메소드


#week03_03.py
age = 21
name = "정석"
temp = 31.5

# f-string
a = f"이름 {name:>10}"
a_1 = f"이름 {name:<10}"
b = f"이름:{name} 나이:{age}"
c = f"온도 {temp}"
d = f"내년 나이 {age + 1}"
print(a); print(a_1); print(b); print(c); print(d)


# str.format() 메소드
a = "이름 {0:>10}".format(name)
b = "이름: {0:<10} 나이:{1:^10}".format(name, age)
c = "온도 {0:0.2f}".format(temp)
print(a); print(b); print(c)

# %-format
a = "내 이름 %10s" % name
b = "이름:%-10s 나이:%d" % (name, age)
c = "온도 %0.1f" % temp
print(a);print(b);print(c)

#인덱싱 
soc_number = input("주민등록번호:") #"1234"
a = soc_number[0]                   #"1"
print(type(a))                      #str
print(id(a))                        #12345
print(id(soc_number))               #1236789

print(soc_number[0], soc_number[-1])
print(soc_number[-len(soc_number)])
print(soc_number[len(soc_number) - 1])

#슬라이싱
a = "abcde"
b = a[1:]
c = a[-3:]
d = a[:2]
e = a[:-1]
f = a[2:4]
g = a[-4:-2]
h = a[:]
print(a);print(b);print(c);print(d);print(e);
print(f);print(g);print(h)


#문자열은 0개 이상의 문자로 구성함.

t1 = 1
t2 = "1"
#a = t1 + t2  숫자+문자열X

a = "" #빈 문자열
b = "I like Python"
c = " " #공백 문자열
print(len(a))
print(len(b))
print(len(c))

a = 3
b = int(2)
print(a/b)
print(a // b)
print(a % b)
