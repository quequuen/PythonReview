#자료형과 기본 연산
#문자열형
#문자열은 불변 자료형이다.(원본 불변)

#문자열 포맷팅

#3. f-string(Formatted String Literals)
name = "김인하"
age = 20
intro = "내 이름은 {name}입니다. 나이는 {age}살입니다."
print(intro)
intro = f"내 이름은 {name}입니다. 나이는 {age}살입니다."
print(intro)
intro = f"내 이름은 {name}입니다. 나이는 {age+1}살입니다."
print(intro)

#2. str.format() 메소드
a = "나는 {0}살입니다.".format(20)
print(a)
age = 21
a = "나는 {0}살입니다.".format(age)
b = "내 이름은 {0} 입니다.".format("인하")
print(a);print(b)
name = "정석"
b = "내 이름은 {0} 입니다.".format(name)
c = "내 이름은 {0}이고, {1}살입니다.".format(name, age)
print(b);print(c)
c = "내 이름은 {name}이고, {age} 살입니다.".format(name = "정석", age =21)
print(c)
c = "내 이름은 {0}이고, {age} 살입니다.".format("정석", age = 21)
print(c)
# str.format() 정렬
a = "'{0:<10}'".format("hi") #왼쪽 정렬
print(a)
a = "'{0:>10}'".format("hi") #오른쪽 정렬
print(a)
a = "'{0:^10}'".format("hi") #가운데 정렬
print(a)
a = "'{0:=^10}'".format("hi") #'====hi===='
print(a)
a = "'{0:!<10}'".format("hi") #'hi!!!!!!!!'
print(a)
print("{0:0.4f}".format(3.141592))

#1. %포맷팅
#old style string formatting(like C Lang)
a = "나는 %d살입니다." %20
print(a)
age=21
a = "나는 %d살입니다." %age
b = "내 이름은 %s 입니다." %"인하"
print(a)
print(b)
name = "정성"
b = "내 이름은 %s 입니다." % name
c = "내 이름은 %s이고, %d 살입니다." %(name, age)
#여러 값을 대입 할 때는 %() 안에 대입할 값 기입
print(b)
print(c)
# %s 는 만능 포맷 코드
#정렬과 공백
temp = 3.14
a = "내 이름 %10s" % name
b = "이름: %-10s 나이: %d" % (name, age)
#-는 왼쪽 정렬 name 뒤에 10칸, 기본은 오른쪽 정렬 name 앞에 10칸
c = "온도 %0.1f" % temp
print(a);print(b);print(c)


a = "I like Python"

#문자열 슬라이싱
print(a[0:4])
print(a[2:6])
print(a[7:])
print(a[:4])
print(a[:])

#문자열 인덱싱
print(a[0])
print(a[-13])
print(a[12])
print(a[-1])
print(a[len(a)-1])

#문자열 관련 연산자&함수
print("a"+"b")
print("a"*3)
print(len("ab"))

#따옴표 안의 따옴표
print("inha's dream")
print("inha\" s dream")
print('inha"s dream')
print('inha\'s dream')

#여러 줄 표현
print("inha \nuniv")
print("""inha
univ""")
print('''inha
univ''')

#문자열 관련 메소드 실습 자료와 ppt 볼 것
